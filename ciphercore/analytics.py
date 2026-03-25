from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import math
import secrets

import numpy as np
from scipy import stats

from ciphercore.utils import sha256_hex


@dataclass
class AnalysisResult:
    title: str
    metrics: dict[str, Any]
    summary: str


def _safe_entropy(probabilities: np.ndarray) -> float:
    non_zero = probabilities[probabilities > 0]
    if non_zero.size == 0:
        return 0.0
    return float(stats.entropy(non_zero, base=2))


def _byte_histogram(data: bytes) -> np.ndarray:
    arr = np.frombuffer(data, dtype=np.uint8)
    if arr.size == 0:
        return np.zeros(256, dtype=np.int64)
    return np.bincount(arr, minlength=256)


def _serial_correlation(data: bytes) -> float:
    arr = np.frombuffer(data, dtype=np.uint8).astype(np.float64)
    if arr.size < 2:
        return 0.0
    a = arr[:-1]
    b = arr[1:]
    if np.std(a) == 0 or np.std(b) == 0:
        return 0.0
    corr = np.corrcoef(a, b)[0, 1]
    if math.isnan(corr):
        return 0.0
    return float(corr)


def _uniform_chi_square(counts: np.ndarray) -> tuple[float, float]:
    total = int(counts.sum())
    if total == 0:
        return 0.0, 1.0
    expected = np.full(256, total / 256.0, dtype=np.float64)
    chi, p_value = stats.chisquare(counts.astype(np.float64), expected)
    return float(chi), float(p_value)


def analyze_text(text: str) -> AnalysisResult:
    encoded = text.encode('utf-8', errors='ignore')
    char_counts = np.array(list({c: text.count(c) for c in set(text)}.values()), dtype=np.float64)
    char_probs = char_counts / char_counts.sum() if char_counts.size else np.array([], dtype=np.float64)
    charset_size = len(set(text))
    entropy_chars = _safe_entropy(char_probs)
    unique_ratio = (charset_size / len(text)) if text else 0.0
    digits = sum(c.isdigit() for c in text)
    letters = sum(c.isalpha() for c in text)
    special = sum(not c.isalnum() and not c.isspace() for c in text)
    whitespace = sum(c.isspace() for c in text)
    metrics = {
        'length_chars': len(text),
        'length_bytes': len(encoded),
        'unique_characters': charset_size,
        'unique_ratio': round(unique_ratio, 4),
        'entropy_bits_per_symbol': round(entropy_chars, 4),
        'letters': letters,
        'digits': digits,
        'special': special,
        'whitespace': whitespace,
        'sha256': sha256_hex(encoded),
    }
    summary = (
        'Higher entropy and a broader character set generally indicate less predictable text, '
        'while repeated structures, low uniqueness and very small alphabets indicate a more structured pattern.'
    )
    return AnalysisResult('text', metrics, summary)


def analyze_password(password: str) -> AnalysisResult:
    base = analyze_text(password)
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 33
    theoretical_entropy = len(password) * math.log2(max(charset, 1)) if password else 0.0
    repeated_pairs = sum(1 for i in range(len(password) - 1) if password[i] == password[i + 1])
    score = 0
    if len(password) >= 10:
        score += 20
    if len(password) >= 16:
        score += 20
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 20
    if any(c.isdigit() for c in password):
        score += 20
    if any(not c.isalnum() for c in password):
        score += 20
    score -= min(repeated_pairs * 3, 15)
    score = max(0, min(score, 100))
    base.metrics.update({
        'theoretical_entropy_bits': round(theoretical_entropy, 2),
        'estimated_charset_size': charset,
        'repeated_adjacent_pairs': repeated_pairs,
        'strength_score': score,
    })
    base.summary = (
        'The score combines length, charset diversity and repetition resistance. '
        'High theoretical entropy with low repetition generally points to a stronger password.'
    )
    return base


def analyze_file(path: Path) -> AnalysisResult:
    raw = path.read_bytes()
    counts = _byte_histogram(raw)
    probabilities = counts / counts.sum() if counts.sum() else np.zeros(256, dtype=np.float64)
    entropy = _safe_entropy(probabilities)
    chi, p_value = _uniform_chi_square(counts)
    serial_corr = _serial_correlation(raw)
    nonzero_bytes = int(np.count_nonzero(counts))
    top_indices = counts.argsort()[-5:][::-1]
    top_bytes = ', '.join(f'{int(idx)}:{int(counts[idx])}' for idx in top_indices if counts[idx] > 0)
    block_size = 4096
    if raw:
        padded = raw + b'\x00' * ((block_size - len(raw) % block_size) % block_size)
        blocks = np.frombuffer(padded, dtype=np.uint8).reshape(-1, block_size)
        block_means = blocks.mean(axis=1)
        block_std = float(np.std(block_means)) if block_means.size else 0.0
    else:
        block_std = 0.0
    metrics = {
        'file_name': path.name,
        'file_size_bytes': len(raw),
        'sha256': sha256_hex(raw),
        'entropy_bits_per_byte': round(entropy, 4),
        'distinct_byte_values': nonzero_bytes,
        'chi_square_uniformity': round(chi, 4),
        'chi_square_p_value': round(p_value, 8),
        'serial_correlation': round(serial_corr, 6),
        'block_mean_stddev': round(block_std, 6),
        'top_byte_frequencies': top_bytes or '-',
    }
    summary = (
        'Encrypted or compressed files often show high byte entropy and a broad byte distribution. '
        'Structured plain data may display lower entropy, stronger repetition and more visible distribution bias.'
    )
    return AnalysisResult('file', metrics, summary)


def compare_files(path_a: Path, path_b: Path) -> AnalysisResult:
    counts_a = _byte_histogram(path_a.read_bytes()).astype(np.float64)
    counts_b = _byte_histogram(path_b.read_bytes()).astype(np.float64)
    norm_a = counts_a / max(counts_a.sum(), 1.0)
    norm_b = counts_b / max(counts_b.sum(), 1.0)
    distance = float(np.linalg.norm(norm_a - norm_b))
    cosine = float(np.dot(norm_a, norm_b) / (np.linalg.norm(norm_a) * np.linalg.norm(norm_b) + 1e-12))
    pearson = float(stats.pearsonr(norm_a, norm_b).statistic) if np.std(norm_a) and np.std(norm_b) else 0.0
    metrics = {
        'file_a': path_a.name,
        'file_b': path_b.name,
        'distribution_distance': round(distance, 8),
        'cosine_similarity': round(cosine, 8),
        'pearson_correlation': round(pearson, 8),
    }
    summary = (
        'The comparison is histogram-based. Higher cosine similarity and correlation indicate more similar '
        'byte distributions, while larger distance indicates stronger structural differences.'
    )
    return AnalysisResult('compare', metrics, summary)


def analyze_random_sample(length: int = 4096) -> AnalysisResult:
    length = max(256, int(length))
    data = secrets.token_bytes(length)
    result = analyze_file_bytes(data, 'generated_random_sample.bin')
    result.summary = (
        'This lab generates fresh cryptographic random data and evaluates its byte distribution. '
        'It is useful for sanity checks and demonstrating the analytics layer.'
    )
    return result


def analyze_file_bytes(raw: bytes, name: str) -> AnalysisResult:
    counts = _byte_histogram(raw)
    probabilities = counts / counts.sum() if counts.sum() else np.zeros(256, dtype=np.float64)
    entropy = _safe_entropy(probabilities)
    chi, p_value = _uniform_chi_square(counts)
    serial_corr = _serial_correlation(raw)
    metrics = {
        'file_name': name,
        'file_size_bytes': len(raw),
        'sha256': sha256_hex(raw),
        'entropy_bits_per_byte': round(entropy, 4),
        'distinct_byte_values': int(np.count_nonzero(counts)),
        'chi_square_uniformity': round(chi, 4),
        'chi_square_p_value': round(p_value, 8),
        'serial_correlation': round(serial_corr, 6),
    }
    return AnalysisResult('file', metrics, 'Randomness-oriented byte profile.')

"""
Utility functions for LocalFlow
"""

import os
from pathlib import Path


def get_file_size(file_path: str) -> str:
    """
    Get human-readable file size
    
    Args:
        file_path: Path to file
    
    Returns:
        File size as string (e.g., "1.5 MB")
    """
    size_bytes = Path(file_path).stat().st_size
    
    # Convert to human-readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    
    return f"{size_bytes:.2f} TB"


def validate_file(file_path: str, allowed_extensions: list) -> bool:
    """
    Validate file exists and has allowed extension
    
    Args:
        file_path: Path to file
        allowed_extensions: List of allowed extensions (e.g., ['.pdf', '.txt'])
    
    Returns:
        True if valid, False otherwise
    """
    # Check if file exists
    if not Path(file_path).exists():
        return False
    
    # Check extension
    file_ext = Path(file_path).suffix.lower()
    return file_ext in allowed_extensions


def create_output_dir(output_dir: str = "output") -> Path:
    """
    Create output directory if it doesn't exist
    
    Args:
        output_dir: Directory name
    
    Returns:
        Path to output directory
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path

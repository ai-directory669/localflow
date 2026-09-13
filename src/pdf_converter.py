"""
PDF to Text Converter
Converts PDF files to text format - 100% offline, privacy-first
"""

import PyPDF2
import pdfplumber
from pathlib import Path


def pdf_to_text_pypdf2(pdf_path: str) -> str:
    """
    Convert PDF to text using PyPDF2
    
    Args:
        pdf_path: Path to PDF file
    
    Returns:
        Extracted text as string
    """
    text = ""
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from all pages
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    return text


def pdf_to_text_pdfplumber(pdf_path: str) -> str:
    """
    Convert PDF to text using pdfplumber (better for complex PDFs)
    
    Args:
        pdf_path: Path to PDF file
    
    Returns:
        Extracted text as string
    """
    text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    return text


def convert_pdf(pdf_path: str, method: str = "pdfplumber") -> str:
    """
    Main function to convert PDF to text
    
    Args:
        pdf_path: Path to PDF file
        method: "pypdf2" or "pdfplumber"
    
    Returns:
        Extracted text as string
    """
    # Check if file exists
    if not Path(pdf_path).exists():
        return "Error: File not found!"
    
    # Check file extension
    if not pdf_path.lower().endswith('.pdf'):
        return "Error: Not a PDF file!"
    
    # Convert based on method
    if method == "pypdf2":
        return pdf_to_text_pypdf2(pdf_path)
    else:
        return pdf_to_text_pdfplumber(pdf_path)


# Test the converter
if __name__ == "__main__":
    # Example usage
    test_pdf = "test.pdf"
    result = convert_pdf(test_pdf)
    print(result)

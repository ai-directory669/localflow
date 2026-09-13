"""
LocalFlow - Privacy-First Local AI Assistant
Main entry point for the application
"""

import sys
from pathlib import Path
from pdf_converter import convert_pdf


def print_banner():
    """Print application banner"""
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║   🚀 LocalFlow - Privacy-First AI Assistant      ║
    ║   100% Offline • No Cloud • No Data Leaks        ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)


def pdf_converter_cli():
    """PDF to Text Converter CLI"""
    print("\n📄 PDF to Text Converter\n")
    
    # Get PDF file path from user
    pdf_path = input("Enter PDF file path: ").strip()
    
    # Check if file exists
    if not Path(pdf_path).exists():
        print("❌ Error: File not found!")
        return
    
    # Convert PDF
    print("⏳ Converting PDF to text...")
    text = convert_pdf(pdf_path)
    
    # Save to file
    output_path = Path(pdf_path).stem + "_converted.txt"
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"\n✅ Success! Text saved to: {output_path}")
        print(f"📊 Total characters: {len(text)}")
    
    except Exception as e:
        print(f"❌ Error saving file: {str(e)}")


def main():
    """Main application"""
    print_banner()
    
    print("\nAvailable tools:")
    print("1. PDF to Text Converter")
    print("2. Exit")
    
    choice = input("\nEnter your choice (1-2): ").strip()
    
    if choice == "1":
        pdf_converter_cli()
    elif choice == "2":
        print("\n👋 Goodbye! Stay private! 🔒")
        sys.exit(0)
    else:
        print("\n❌ Invalid choice!")


if __name__ == "__main__":
    main()

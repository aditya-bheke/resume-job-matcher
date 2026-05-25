# Import library used for reading PDF files
import pdfplumber


# Function to extract text from a PDF resume
def extract_text_from_pdf(pdf_path):

    # Empty string to store all extracted text
    text = ""

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:

        # Loop through every page in the PDF
        for page in pdf.pages:

            # Extract text from current page
            extracted = page.extract_text()

            # Some pages may return None
            # Only add text if extraction succeeded
            if extracted:

                # Add extracted page text to final text
                text += extracted + "\n"

    # Return complete extracted resume text
    return text
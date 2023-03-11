import PyPDF2
import tiktoken


def pdf_to_string_array(pdf_path):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        num_pages = len(pdf_reader.pages)

        strings = []

        for page_num in range(num_pages):
            page_obj = pdf_reader.pages[page_num]

            words = page_obj.extract_text().split()

            current_string = ""

            for word in words:
                current_string += word + " "

                if (len(encoding.encode(current_string))) >= 1500:
                    strings.append(current_string.strip())
                    current_string = ""

            if current_string != "":
                strings.append(current_string.strip())
    # Print the list of strings
    return strings

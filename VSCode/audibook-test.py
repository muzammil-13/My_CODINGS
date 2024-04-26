import PyPDF2
import pyttsx3
# Read the pdf by specifying the path in your computer 
pdfReader = PyPDF2.PdfFileReader(open("C:\Users\Public\Documents\Interview Tips.pdf", 'rb'))
# Get the handle to speaker
speaker = pyttsx3.init()
# split the pages and read one by one
for page_num in range(pdfReader.numPages): 
    text = pdfReader.getPage(page_num).extractText() 
    speaker.say(text)
    speaker.runAndWait()
# stop the speaker after completion 
speaker.stop() 
# save the audiobook at specified path 
engine.save_to_file(text, r"C:\Users\Public\Music\audiobook-test.mpe")
engine.runAndWait()

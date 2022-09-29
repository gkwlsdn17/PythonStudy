from docx2pdf import convert

class Convert2PDF:
    def __init__(self, name, birth, ho):
        self.name = name
        self.birth = birth
        self.ho = ho

    def convert(self):
        convert(f'{self.name} certification.docx', f'{self.name}_{self.birth}_{self.ho}.pdf')
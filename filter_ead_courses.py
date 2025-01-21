import requests

institutions_uri = 'https://sisu-api.sisu.mec.gov.br/api/v1/oferta/instituicoes'
institution_offers_uri = 'https://sisu-api.sisu.mec.gov.br/api/v1/oferta/instituicao/{co_ies}'

class Course:
    def __init__(self, course_name, ies, estado, campus):
        self.course_name = course_name
        self.ies = ies
        self.estado = estado
        self.campus = campus
    
    def __str__(self):
        return f'{self.course_name} -> {self.ies} ({self.estado}) | CAMPUS: {self.campus}'

def get_institutions_data():
   response = requests.get(institutions_uri)
   return response.json()

def get_institution_offers_data(institution):
    try:
        offers_data = requests.get(institution_offers_uri.replace("{co_ies}", institution["co_ies"]))
    except:
        print('deu erro')
    offers_json = offers_data.json()

    for index, offer in offers_json.items():
        if index.isdigit():
            if offer["co_turno"] == '10069': 
                course = Course(course_name=offer["no_curso"], ies=offer["no_ies"], estado=offer["sg_uf_ies"], campus=offer["no_campus"])
                print(course)

def run():
    institutions_data = get_institutions_data()

    for institution in institutions_data:
        get_institution_offers_data(institution)

run()

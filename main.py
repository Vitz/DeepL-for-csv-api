import requests
import csv


class ApiTranslator:
    def __init__(self, api_key, target_lang, source_lang):
        self.api_key = api_key
        self.target_lang = target_lang
        self.source_lang = source_lang
        self.host = 'https://api.deepl.com/v2/'

    def translate_csv_file(self, filename, columns, index_col):
        with open("out.csv", 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns + [index_col])
            writer.writeheader()

        data_to_translate = self.read_file(columns, filename, index_col)
        for item in data_to_translate:
            tanslated_elem = {}
            tanslated_elem[index_col] = item[index_col]
            for column in columns:
                value =  str(item[column]).replace("\\n","\r\n")
                translated_sentence = self.trasnalate_text(value)
                tanslated_elem[column] = translated_sentence

            with open("out.csv", 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=columns + [index_col])
                writer.writerow(tanslated_elem)


    def read_file(self, columns, filename, index_col):
        data = []
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                selected_cols = {}
                columns_read = columns + [index_col]
                for column in columns_read:
                    selected_cols[column] = row[column]
                data.append(selected_cols)
        return data

    def trasnalate_text(self, text):
        query_list =[]
        query_list.append("translate?auth_key=" + self.api_key)
        query_list.append("text=\'" + text+"\'")
        query_list.append("target_lang=" + self.target_lang)
        query_list.append("source_lang=" + self.source_lang)
        return  self.__request("&".join(query_list))

    def test(self):
        query = "usage?auth_key=" + self.api_key
        return self.__request(query)


    def __request(self, query=None):
        resp = requests.get(self.host + query)
        if resp.status_code != 200:
            print("Erorr-> " + query)
            pass # save error
        json_response = resp.json()
        return json_response["translations"][0]["text"]

at = ApiTranslator(api_key= 'y', target_lang="PL", source_lang="EN")
# print(str(at.test()))
tr = at.translate_csv_file(filename= "prods.csv" , columns = ["Name", "Description"], index_col = "SKU")
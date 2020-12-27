# DeepL-api  
It's a short program to make CSV translation process more easy. You will be able to translate selected columns from your CSV file.     
  
  
Example of using:   
at = ApiTranslator(api_key= 'y', target_lang="PL", source_lang="EN")  
tr = at.translate_csv_file(filename= "prods.csv" , columns = ["Name", "Description"], index_col = "SKU")
  
  
Explanation:  
Program will open your CSV file and save new text (translated data via DeepL) based on provided name list eg.:
columns = ["Name", "Description"]  
  
Remember to use column with indexes eg.:  
index_col = "SKU"  
In tested case SKU was an internal product code (string type).  
  
After execute program, there will be created a new file named out.csv with the sam indexes as a result.  





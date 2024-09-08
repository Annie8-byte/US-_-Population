import duckdb

duckdb.read_csv("test.csv")              
result = duckdb.sql("SELECT * FROM 'test.csv'")    

print(result)
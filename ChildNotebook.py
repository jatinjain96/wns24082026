# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Child notebook code
print("Hello from ChildNotebook!")
dbutils.notebook.exit("Success")

# COMMAND ----------

dbutils.widgets.dropdown(
    name="tech", defaultValue="5g", choices=["5g", "10g", "13g", "11g"], label="My tech"
)
 
dbutils.widgets.text(name = "name", defaultValue="John", label="My name")

# COMMAND ----------

print(dbutils.widgets.get("tech"))
print(dbutils.widgets.get("name"))

# COMMAND ----------


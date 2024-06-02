import os
import pytest
import sanskriti_bench.db.crud_functions as crud 
import sanskriti_bench.settings as settings

@pytest.fixture(scope="module")
def setup_database():
    # Set up the database and tables
    crud.create_database(database_name=settings.DB_NAME)
    crud.create_table(table_name="bengali", database_name=settings.DB_NAME)
    crud.create_table(table_name="hindi", database_name=settings.DB_NAME)
    yield
    # Teardown: Drop tables and delete database
    os.remove("sanskriti_bench_test.db")

@pytest.fixture(scope="module")
def insert_data(setup_database):
    # Insert test data
    items = [
        {"email": "anindya@gmail.com", "lang": "bengali", "contri": "সূর্য আসছে এবং দিনের শুরু হচ্ছে।"},
        {"email": "anindya@gmail.com", "lang": "bengali", "contri": "মেঘ আসছে আকাশে।"},
        {"email": "archisman@gmail.com", "lang": "bengali", "contri": "পাখি গান গাইতে সুরমা দেয়।"},
        {"email": "kola@gmail.com", "lang": "hindi", "contri": "सूरज उग रहा है और दिन की शुरुआत हो रही है।"},
        {"email": "uni@gmail.com", "lang": "hindi", "contri": "आसमान में बादल आ रहे हैं।"},
        {"email": "uni@gmail.com", "lang": "hindi", "contri": "पक्षी गाने में संगीत का जादू बिखेर रहे हैं।"},
    ]
    for item in items:
        crud.insert(database_name=settings.DB_NAME, table_name=item["lang"], values={
            "contributor_email": item["email"],
            "language": item["lang"], 
            "question": item["contri"],
            "answer": item["contri"]
        })

@pytest.fixture(scope="module")
def export_csv(setup_database, insert_data):
    # Export data to CSV
    folder_path = "/tmp"
    crud.export_data_to_csv(
        database_name=settings.DB_NAME, 
        table_name="bengali", 
        csv_file_path=os.path.join(folder_path, settings.EXPORT_CSV_FILE_PATH.format(language="bengali"))
    )
    crud.export_data_to_csv(
        database_name=settings.DB_NAME, 
        table_name="hindi", 
        csv_file_path=os.path.join(folder_path, settings.EXPORT_CSV_FILE_PATH.format(language="hindi"))
    )

def test_export_csv(export_csv):
    # Test CSV export
    folder_path = "/tmp"
    assert os.path.exists(os.path.join(folder_path, settings.EXPORT_CSV_FILE_PATH.format(language="bengali")))
    assert os.path.exists(os.path.join(folder_path, settings.EXPORT_CSV_FILE_PATH.format(language="hindi")))

def test_get_total_contributions_across_all_languages(insert_data):
    # Test total contributions across all languages
    total_contributions = crud.get_total_contributions_across_all_languages(database_name=settings.DB_NAME)
    print("=========")
    crud.read_table(settings.DB_NAME, table_name="bengali")
    print("\n")
    crud.read_table(settings.DB_NAME, table_name="hindi")
    print("=========")
    print("\n\n")
    assert total_contributions == 6

def test_get_total_contributions_single_language(insert_data):
    # Test total contributions for each language
    hindi_contributions = crud.get_total_contributions_single_language(database_name=settings.DB_NAME, table_name="hindi")
    bengali_contributions = crud.get_total_contributions_single_language(database_name=settings.DB_NAME, table_name="bengali")
    assert hindi_contributions == 3
    assert bengali_contributions == 3

def test_get_total_contributions_by_contributor(insert_data):
    # Test total contributions by specific contributors
    assert crud.get_total_contributions_by_contributor(database_name=settings.DB_NAME, table_name="hindi", email="uni@gmail.com") == 2
    assert crud.get_total_contributions_by_contributor(database_name=settings.DB_NAME, table_name="bengali", email="anindya@gmail.com") == 2


-- List all tables in alx_book_store database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'alx_book_store';
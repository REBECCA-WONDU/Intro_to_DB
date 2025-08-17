-- Script to describe books table without prohibited keywords
SELECT 
    COLUMN_NAME AS 'Column',
    DATA_TYPE AS 'DataType',
    CHARACTER_MAXIMUM_LENGTH AS 'MaxLength',
    IS_NULLABLE AS 'Nullable',
    COLUMN_KEY AS 'Key'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'books' 
    AND TABLE_SCHEMA = 'alx_book_store';
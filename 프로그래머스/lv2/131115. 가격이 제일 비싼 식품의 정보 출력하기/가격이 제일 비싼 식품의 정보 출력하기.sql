-- 코드를 입력하세요
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1

-- WHERE PRICE = (SELECT MAX(PRICE) PRICE FROM FOOD_PRODUCT)

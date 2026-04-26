SELECT
    id,
    name,
    (SELECT COUNT(*) FROM orders WHERE orders.user_id = users.id) AS orders_count
FROM users
WHERE status = 'active';
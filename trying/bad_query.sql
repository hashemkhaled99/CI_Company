select 
    id,
    name,
    (select count(*) from orders where orders.user_id = users.id)
from users
where status = 'active'
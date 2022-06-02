# Shoppping list views #

## Create shopping list ##
Только авторизованный пользователь<br>
url - /shopping-list/create<br>
json-request-data: shopping_list_name

## Добавить пункт в список покупок ##
Только авторизованный пользователь, являющийся участником списка<br>
url - /shopping-list/shopping-list-name=<>/add-item<br>
json-request-data: new_list_item, description

## Редактировать пункт списка ##
Только авторизованный пользователь, являющийся участником списк и добавивший этот пункт списка<br>
url - /shopping-list/shopping-list-name=<>/edit-list-item<br>
json-request-data: list_item, new_list_item(опционально), new_description(опционально)

## Удалить пункт списка ##
Только авторизованный пользователь, являющийся участником списка<br>
url - /shoppping-list/shopping-list-name=<>/delete-list-item<br>
json-request-data: list-item

## Весь список ##
Только авторизованный пользователь, являющийся участником списка<br>
url - /shopping-list/shopping-list-name=<название группы>/all-items<br>
get-запрос<br>

## Отдельный пункт списка ##
Только авторизованный пользователь, являющийся участником списка<br>
url - /shopping-list/shopping-list-name=<название группы>/list-item=<пункт списка><br>
get-запрос

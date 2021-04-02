# CONOMY_TEST


RESTful API service


# Run application

1. With docker: `docker-compose up` (docker should be installed)

Application will be available at http://127.0.0.1

# Request example

`GET /api/wallets/`

##### Список кошельков.

http://localhost//api/wallets/  



`POST /api/add_wallet/`

##### Создание кошелька.

http://localhost/api/add_wallet/

Пример JSON для запроса:
  
 
```

{
    "name": "My first wallet"
    
}

```

`PUT /api/update_wallet/<int:pk>/`

##### Редактирование кошелька.

http://localhost/api/update_wallet/1/

Пример JSON для запроса:
  
 
```

{
    "name": "My new first wallet"
    
}

```
`DELETE /api/delete_wallet/<int:pk>/`

##### Удаление кошелька.

http://localhost/api/delete_wallet/1/



`GET /api/transactions/`

##### Получение списка транзакций.

http://localhost/api/transactions/

`POST /api/add_transaction/`

##### Создание транзакции.

http://localhost/api/add_transaction/

Пример JSON для запроса: 
 
```

{
    
    "wallet": 1,
    "amount": 1000.00,
    "description": "For shopping"
    
}

```

`DELETE /api/delete_transaction/<int:pk>/`

##### Удаление транзакции.

http://localhost/api/delete_transaction/1/


`GET /api/transactions/<int:pk>/`

##### Получение списка транзакций по ID кошелька.

http://localhost/api/transactions/1/


```
Задание:
Пишем простой REST сервис (на Django).
Подразумевается, что под ваш REST сервис будет написано отдельное приложение (SPA или мобильное).

Сервис по управлению финансами, функционал следующий:
- Пользователь хранит данные о своем "кошельке", произвольное название + баланс в рублях.
- В рамках кошелька ведется история транзакций (как списание, так и пополнение).
- Кошельков может быть больше чем 1, но сам пользователь один (это его персональный веб сервис).

API сервиса должен позволять:
1. создавать, редактировать и удалять кошелек.
2. создавать и удалять транзакции в рамках кошелька (при этом напрямую редактировать баланс кошелька пользователь не может)
транзакции могут быть как +, так и -. то есть транзакции по зачислению денег и списанию.
у каждой транзакции должна быть дата, сумма, произвольный комментарий от пользователя.
3. Просматривать список своих кошельков
4. Просматривать список своих транзакций как в рамках одного кошелька, так и общий, всех кошельков сразу.

По итогу нужно предоставить исходники сервиса, чтобы мы могли его развернуть (git) и запустить
```
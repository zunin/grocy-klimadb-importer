import requests
from typing import TypedDict, List, Any, Literal, Union

class SYSTEM_INFO:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/system/info',
        )


class SYSTEM_DB_CHANGED_TIME:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/system/db-changed-time',
        )


class SYSTEM_CONFIG:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/system/config',
        )


class SYSTEM_TIME:
    @classmethod
    def GET(cls, offset: int=None) -> requests.Request:
        """
        :param offset: Offset of timestamp in seconds. Can be positive or negative.
        """
        return requests.Request(
            method='GET',
            url=f'/system/time',
            params={'offset': offset},
        )


class SYSTEM_LOCALIZATION_STRINGS:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/system/localization-strings',
        )


class SYSTEM_LOG_MISSING_LOCALIZATION:
    MissingLocalizationRequest = TypedDict('MissingLocalizationRequest', text=str)
    @classmethod
    def POST(cls, body: MissingLocalizationRequest) -> requests.Request:
        """
        Only when MODE == 'dev', so should only be called then
        """
        return requests.Request(
            method='POST',
            url=f'/system/log-missing-localization',
            json=body,
        )


class OBJECTS_BY_ENTITY:
    @classmethod
    def GET(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "userfields", "userentities", "userobjects", "meal_plan", "stock_log", "stock", "stock_current_locations", "chores_log", "meal_plan_sections"], query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param entity: A valid entity name
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/objects/{entity}',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )
    Product = TypedDict('Product', id=int, name=str, description=str, location_id=int, qu_id_purchase=int, qu_id_stock=int, enable_tare_weight_handling=int, not_check_stock_fulfillment_for_recipes=int, product_group_id=int, qu_factor_purchase_to_stock=int, tare_weight=int, barcode=str, min_stock_amount=int, default_best_before_days=int, default_best_before_days_after_open=int, picture_file_name=str, row_created_timestamp=str, shopping_location_id=int, userfields=dict[str, Any])
    Chore = TypedDict('Chore', id=int, name=str, description=str, period_type=Literal["manually", "dynamic-regular", "daily", "weekly", "monthly"], period_config=str, period_days=int, track_date_only=bool, rollover=bool, assignment_type=Literal["no-assignment", "who-least-did-first", "random", "in-alphabetical-order"], assignment_config=str, next_execution_assigned_to_user_id=int, row_created_timestamp=str, userfields=dict[str, Any])
    Battery = TypedDict('Battery', id=int, name=str, description=str, used_in=str, charge_interval_days=int, row_created_timestamp=str, userfields=dict[str, Any])
    Location = TypedDict('Location', id=int, name=str, description=str, row_created_timestamp=str, userfields=dict[str, Any])
    QuantityUnit = TypedDict('QuantityUnit', id=int, name=str, name_plural=str, description=str, row_created_timestamp=str, plural_forms=str, userfields=dict[str, Any])
    ShoppingListItem = TypedDict('ShoppingListItem', id=int, shopping_list_id=int, product_id=int, note=str, amount=int, row_created_timestamp=str, userfields=dict[str, Any])
    StockEntry = TypedDict('StockEntry', id=int, product_id=int, location_id=int, shopping_location_id=int, amount=int, best_before_date=str, purchased_date=str, stock_id=str, price=int, open=int, opened_date=str, row_created_timestamp=str)
    ProductBarcode = TypedDict('ProductBarcode', product_id=int, barcode=str, qu_id=int, shopping_location_id=int, amount=int, last_price=int, note=str)
    @classmethod
    def POST(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "userfields", "userentities", "userobjects", "meal_plan", "meal_plan_sections"], body: Union[Product, Chore, Battery, Location, QuantityUnit, ShoppingListItem, StockEntry, ProductBarcode]) -> requests.Request:
        """
        :param entity: A valid entity name
        """
        return requests.Request(
            method='POST',
            url=f'/objects/{entity}',
            json=body,
        )


class OBJECTS_BY_ENTITY_BY_OBJECTID:
    @classmethod
    def GET(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "userfields", "userentities", "userobjects", "meal_plan", "stock_log", "stock", "stock_current_locations", "chores_log", "meal_plan_sections"], objectId: int) -> requests.Request:
        """
        :param entity: A valid entity name
        :param objectId: A valid object id of the given entity
        """
        return requests.Request(
            method='GET',
            url=f'/objects/{entity}/{objectId}',
        )
    Product = TypedDict('Product', id=int, name=str, description=str, location_id=int, qu_id_purchase=int, qu_id_stock=int, enable_tare_weight_handling=int, not_check_stock_fulfillment_for_recipes=int, product_group_id=int, qu_factor_purchase_to_stock=int, tare_weight=int, barcode=str, min_stock_amount=int, default_best_before_days=int, default_best_before_days_after_open=int, picture_file_name=str, row_created_timestamp=str, shopping_location_id=int, userfields=dict[str, Any])
    Chore = TypedDict('Chore', id=int, name=str, description=str, period_type=Literal["manually", "dynamic-regular", "daily", "weekly", "monthly"], period_config=str, period_days=int, track_date_only=bool, rollover=bool, assignment_type=Literal["no-assignment", "who-least-did-first", "random", "in-alphabetical-order"], assignment_config=str, next_execution_assigned_to_user_id=int, row_created_timestamp=str, userfields=dict[str, Any])
    Battery = TypedDict('Battery', id=int, name=str, description=str, used_in=str, charge_interval_days=int, row_created_timestamp=str, userfields=dict[str, Any])
    Location = TypedDict('Location', id=int, name=str, description=str, row_created_timestamp=str, userfields=dict[str, Any])
    QuantityUnit = TypedDict('QuantityUnit', id=int, name=str, name_plural=str, description=str, row_created_timestamp=str, plural_forms=str, userfields=dict[str, Any])
    ShoppingListItem = TypedDict('ShoppingListItem', id=int, shopping_list_id=int, product_id=int, note=str, amount=int, row_created_timestamp=str, userfields=dict[str, Any])
    StockEntry = TypedDict('StockEntry', id=int, product_id=int, location_id=int, shopping_location_id=int, amount=int, best_before_date=str, purchased_date=str, stock_id=str, price=int, open=int, opened_date=str, row_created_timestamp=str)
    ProductBarcode = TypedDict('ProductBarcode', product_id=int, barcode=str, qu_id=int, shopping_location_id=int, amount=int, last_price=int, note=str)
    @classmethod
    def PUT(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "userfields", "userentities", "userobjects", "meal_plan", "meal_plan_sections"], objectId: int, body: Union[Product, Chore, Battery, Location, QuantityUnit, ShoppingListItem, StockEntry, ProductBarcode]) -> requests.Request:
        """
        :param entity: A valid entity name
        :param objectId: A valid object id of the given entity
        """
        return requests.Request(
            method='PUT',
            url=f'/objects/{entity}/{objectId}',
            json=body,
        )
    @classmethod
    def DELETE(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "api_keys", "userfields", "userentities", "userobjects", "meal_plan", "meal_plan_sections"], objectId: int) -> requests.Request:
        """
        :param entity: A valid entity name
        :param objectId: A valid object id of the given entity
        """
        return requests.Request(
            method='DELETE',
            url=f'/objects/{entity}/{objectId}',
        )


class USERFIELDS_BY_ENTITY_BY_OBJECTID:
    @classmethod
    def GET(cls, entity: Literal["products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "api_keys", "userfields", "userentities", "userobjects", "meal_plan", "stock_log", "stock", "stock_current_locations", "chores_log", "meal_plan_sections", "api_keys", "batteries", "chores", "chores_log", "equipment", "locations", "meal_plan", "meal_plan_sections", "product_barcodes", "product_groups", "products", "quantity_unit_conversions", "quantity_units", "recipes", "recipes_nestings", "recipes_pos", "shopping_list", "shopping_lists", "shopping_locations", "stock", "stock_current_locations", "stock_log", "task_categories", "tasks", "userentities", "userfields", "userobjects", "users"], objectId: int) -> requests.Request:
        """
        :param entity: A valid entity name
        :param objectId: A valid object id of the given entity
        """
        return requests.Request(
            method='GET',
            url=f'/userfields/{entity}/{objectId}',
        )
    @classmethod
    def PUT(cls, entity: Literal["", "products", "chores", "product_barcodes", "batteries", "locations", "quantity_units", "quantity_unit_conversions", "shopping_list", "shopping_lists", "shopping_locations", "recipes", "recipes_pos", "recipes_nestings", "tasks", "task_categories", "product_groups", "equipment", "userfields", "userentities", "userobjects", "meal_plan", "meal_plan_sections", "batteries", "chores", "equipment", "locations", "meal_plan", "meal_plan_sections", "product_barcodes", "product_groups", "products", "quantity_unit_conversions", "quantity_units", "recipes", "recipes_nestings", "recipes_pos", "shopping_list", "shopping_lists", "shopping_locations", "task_categories", "tasks", "userentities", "userfields", "userobjects", "users"], objectId: int, body: Any) -> requests.Request:
        """
        :param entity: A valid entity name
        :param objectId: A valid object id of the given entity
        """
        return requests.Request(
            method='PUT',
            url=f'/userfields/{entity}/{objectId}',
            json=body,
        )


class FILES_BY_GROUP_BY_FILENAME:
    @classmethod
    def GET(cls, group: Literal["equipmentmanuals", "recipepictures", "productpictures", "userfiles", "userpictures"], fileName: str, force_serve_as: Literal["picture"]=None, best_fit_height: int=None, best_fit_width: int=None) -> requests.Request:
        """
        With proper Content-Type header
        """
        return requests.Request(
            method='GET',
            url=f'/files/{group}/{fileName}',
            params={'force_serve_as': force_serve_as, 'best_fit_height': best_fit_height, 'best_fit_width': best_fit_width},
        )
    @classmethod
    def PUT(cls, group: Literal["equipmentmanuals", "recipepictures", "productpictures", "userfiles", "userpictures"], fileName: str) -> requests.Request:
        """
        The file will be stored at /data/storage/{group}/{file_name} (you need to remember the group and file name to get or delete it again)
        """
        return requests.Request(
            method='PUT',
            url=f'/files/{group}/{fileName}',
        )
    @classmethod
    def DELETE(cls, group: Literal["equipmentmanuals", "recipepictures", "productpictures", "userfiles", "userpictures"], fileName: str) -> requests.Request:
        """
        :param group: The file group
        :param fileName: The file name (including extension)<br>**BASE64 encoded**
        """
        return requests.Request(
            method='DELETE',
            url=f'/files/{group}/{fileName}',
        )


class USERS:
    @classmethod
    def GET(cls, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/users',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )
    User = TypedDict('User', id=int, username=str, first_name=str, last_name=str, password=str, picture_file_name=str, row_created_timestamp=str)
    @classmethod
    def POST(cls, body: User) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/users',
            json=body,
        )


class USERS_BY_USERID:
    User = TypedDict('User', id=int, username=str, first_name=str, last_name=str, password=str, picture_file_name=str, row_created_timestamp=str)
    @classmethod
    def PUT(cls, userId: int, body: User) -> requests.Request:
        """
        :param userId: A valid user id
        """
        return requests.Request(
            method='PUT',
            url=f'/users/{userId}',
            json=body,
        )
    @classmethod
    def DELETE(cls, userId: int) -> requests.Request:
        """
        :param userId: A valid user id
        """
        return requests.Request(
            method='DELETE',
            url=f'/users/{userId}',
        )


class USERS_BY_USERID_PERMISSIONS:
    @classmethod
    def GET(cls, userId: int) -> requests.Request:
        """
        :param userId: A valid user id
        """
        return requests.Request(
            method='GET',
            url=f'/users/{userId}/permissions',
        )
    Body = TypedDict('Body', permissions_id=int)
    @classmethod
    def POST(cls, userId: int, body: Body) -> requests.Request:
        """
        :param userId: A valid user id
        """
        return requests.Request(
            method='POST',
            url=f'/users/{userId}/permissions',
            json=body,
        )
    Body = TypedDict('Body', permissions=List[int])
    @classmethod
    def PUT(cls, userId: int, body: Body) -> requests.Request:
        """
        :param userId: A valid user id
        """
        return requests.Request(
            method='PUT',
            url=f'/users/{userId}/permissions',
            json=body,
        )


class USER:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/user',
        )


class USER_SETTINGS:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/user/settings',
        )


class USER_SETTINGS_BY_SETTINGKEY:
    @classmethod
    def GET(cls, settingKey: str) -> requests.Request:
        """
        :param settingKey: The key of the user setting
        """
        return requests.Request(
            method='GET',
            url=f'/user/settings/{settingKey}',
        )
    UserSetting = TypedDict('UserSetting', value=str)
    @classmethod
    def PUT(cls, settingKey: str, body: UserSetting) -> requests.Request:
        """
        :param settingKey: The key of the user setting
        """
        return requests.Request(
            method='PUT',
            url=f'/user/settings/{settingKey}',
            json=body,
        )
    @classmethod
    def DELETE(cls, settingKey: str) -> requests.Request:
        """
        :param settingKey: The key of the user setting
        """
        return requests.Request(
            method='DELETE',
            url=f'/user/settings/{settingKey}',
        )


class STOCK:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/stock',
        )


class STOCK_ENTRY_BY_ENTRYID:
    @classmethod
    def GET(cls, entryId: int) -> requests.Request:
        """
        :param entryId: A valid stock entry id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/entry/{entryId}',
        )
    Body = TypedDict('Body', amount=int, best_before_date=str, price=int, open=bool, location_id=int, shopping_location_id=int, purchased_date=str)
    @classmethod
    def PUT(cls, entryId: int, body: Body) -> requests.Request:
        """
        :param entryId: A valid stock entry id
        """
        return requests.Request(
            method='PUT',
            url=f'/stock/entry/{entryId}',
            json=body,
        )


class STOCK_ENTRY_BY_ENTRYID_PRINTLABEL:
    @classmethod
    def GET(cls, entryId: int) -> requests.Request:
        """
        :param entryId: A valid stock entry id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/entry/{entryId}/printlabel',
        )


class STOCK_VOLATILE:
    @classmethod
    def GET(cls, due_soon_days: int=5) -> requests.Request:
        """
        :param due_soon_days: The number of days in which products are considered to be due soon
        """
        return requests.Request(
            method='GET',
            url=f'/stock/volatile',
            params={'due_soon_days': due_soon_days},
        )


class STOCK_PRODUCTS_BY_PRODUCTID:
    @classmethod
    def GET(cls, productId: int) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/{productId}',
        )


class STOCK_PRODUCTS_BY_PRODUCTID_LOCATIONS:
    @classmethod
    def GET(cls, productId: int, include_sub_products: bool=None, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param productId: A valid product id
        :param include_sub_products: If sub product locations should be included (if the given product is a parent product and in addition to the ones of the given product)
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/{productId}/locations',
            params={'include_sub_products': include_sub_products, 'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class STOCK_PRODUCTS_BY_PRODUCTID_ENTRIES:
    @classmethod
    def GET(cls, productId: int, include_sub_products: bool=None, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param productId: A valid product id
        :param include_sub_products: If sub products should be included (if the given product is a parent product and in addition to the ones of the given product)
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/{productId}/entries',
            params={'include_sub_products': include_sub_products, 'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class STOCK_PRODUCTS_BY_PRODUCTID_PRICE_HISTORY:
    @classmethod
    def GET(cls, productId: int) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/{productId}/price-history',
        )


class STOCK_PRODUCTS_BY_PRODUCTID_ADD:
    Body = TypedDict('Body', amount=int, best_before_date=str, transaction_type=Literal["purchase", "consume", "inventory-correction", "product-opened"], price=int, location_id=int, shopping_location_id=int, stock_label_type=int)
    @classmethod
    def POST(cls, productId: int, body: Body) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productId}/add',
            json=body,
        )


class STOCK_PRODUCTS_BY_PRODUCTID_CONSUME:
    Body = TypedDict('Body', amount=int, transaction_type=Literal["purchase", "consume", "inventory-correction", "product-opened"], spoiled=bool, stock_entry_id=str, recipe_id=int, location_id=int, exact_amount=bool, allow_subproduct_substitution=bool)
    @classmethod
    def POST(cls, productId: int, body: Body) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productId}/consume',
            json=body,
        )


class STOCK_PRODUCTS_BY_PRODUCTID_TRANSFER:
    Body = TypedDict('Body', amount=int, location_id_from=int, location_id_to=int, stock_entry_id=str)
    @classmethod
    def POST(cls, productId: int, body: Body) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productId}/transfer',
            json=body,
        )


class STOCK_PRODUCTS_BY_PRODUCTID_INVENTORY:
    Body = TypedDict('Body', new_amount=int, best_before_date=str, shopping_location_id=int, location_id=int, price=int)
    @classmethod
    def POST(cls, productId: int, body: Body) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productId}/inventory',
            json=body,
        )


class STOCK_PRODUCTS_BY_PRODUCTID_OPEN:
    Body = TypedDict('Body', amount=int, stock_entry_id=str, allow_subproduct_substitution=bool)
    @classmethod
    def POST(cls, productId: int, body: Body) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productId}/open',
            json=body,
        )


class STOCK_PRODUCTS_BY_PRODUCTID_PRINTLABEL:
    @classmethod
    def GET(cls, productId: int) -> requests.Request:
        """
        :param productId: A valid product id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/{productId}/printlabel',
        )


class STOCK_PRODUCTS_BY_PRODUCTIDTOKEEP_MERGE_BY_PRODUCTIDTOREMOVE:
    @classmethod
    def POST(cls, productIdToKeep: int, productIdToRemove: int) -> requests.Request:
        """
        :param productIdToKeep: A valid product id of the product to keep
        :param productIdToRemove: A valid product id of the product to remove
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/{productIdToKeep}/merge/{productIdToRemove}',
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE:
    @classmethod
    def GET(cls, barcode: str) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='GET',
            url=f'/stock/products/by-barcode/{barcode}',
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE_ADD:
    Body = TypedDict('Body', amount=int, best_before_date=str, transaction_type=Literal["purchase", "consume", "inventory-correction", "product-opened"], price=int, location_id=int)
    @classmethod
    def POST(cls, barcode: str, body: Body) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/by-barcode/{barcode}/add',
            json=body,
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE_CONSUME:
    Body = TypedDict('Body', amount=int, transaction_type=Literal["purchase", "consume", "inventory-correction", "product-opened"], spoiled=bool, stock_entry_id=str, recipe_id=int, location_id=int, exact_amount=bool, allow_subproduct_substitution=bool)
    @classmethod
    def POST(cls, barcode: str, body: Body) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/by-barcode/{barcode}/consume',
            json=body,
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE_TRANSFER:
    Body = TypedDict('Body', amount=int, location_id_from=int, location_id_to=int, stock_entry_id=str)
    @classmethod
    def POST(cls, barcode: str, body: Body) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/by-barcode/{barcode}/transfer',
            json=body,
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE_INVENTORY:
    Body = TypedDict('Body', new_amount=int, best_before_date=str, location_id=int, price=int)
    @classmethod
    def POST(cls, barcode: str, body: Body) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/by-barcode/{barcode}/inventory',
            json=body,
        )


class STOCK_PRODUCTS_BY_BARCODE_BY_BARCODE_OPEN:
    Body = TypedDict('Body', amount=int, stock_entry_id=str, allow_subproduct_substitution=bool)
    @classmethod
    def POST(cls, barcode: str, body: Body) -> requests.Request:
        """
        :param barcode: Barcode
        """
        return requests.Request(
            method='POST',
            url=f'/stock/products/by-barcode/{barcode}/open',
            json=body,
        )


class STOCK_SHOPPINGLIST_ADD_MISSING_PRODUCTS:
    Body = TypedDict('Body', list_id=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/add-missing-products',
            json=body,
        )


class STOCK_SHOPPINGLIST_ADD_OVERDUE_PRODUCTS:
    Body = TypedDict('Body', list_id=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/add-overdue-products',
            json=body,
        )


class STOCK_SHOPPINGLIST_ADD_EXPIRED_PRODUCTS:
    Body = TypedDict('Body', list_id=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/add-expired-products',
            json=body,
        )


class STOCK_SHOPPINGLIST_CLEAR:
    Body = TypedDict('Body', list_id=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/clear',
            json=body,
        )


class STOCK_SHOPPINGLIST_ADD_PRODUCT:
    Body = TypedDict('Body', product_id=int, list_id=int, product_amount=int, note=str)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        """
        If the product is already on the shopping list, the given amount will increase the amount of the already existing item, otherwise a new item will be added
        """
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/add-product',
            json=body,
        )


class STOCK_SHOPPINGLIST_REMOVE_PRODUCT:
    Body = TypedDict('Body', product_id=int, list_id=int, product_amount=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        """
        If the resulting amount is <= 0, the item will be completely removed from the given list, otherwise the given amount will reduce the amount of the existing item
        """
        return requests.Request(
            method='POST',
            url=f'/stock/shoppinglist/remove-product',
            json=body,
        )


class STOCK_BOOKINGS_BY_BOOKINGID:
    @classmethod
    def GET(cls, bookingId: int) -> requests.Request:
        """
        :param bookingId: A valid stock booking id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/bookings/{bookingId}',
        )


class STOCK_BOOKINGS_BY_BOOKINGID_UNDO:
    @classmethod
    def POST(cls, bookingId: int) -> requests.Request:
        """
        :param bookingId: A valid stock booking id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/bookings/{bookingId}/undo',
        )


class STOCK_TRANSACTIONS_BY_TRANSACTIONID:
    @classmethod
    def GET(cls, transactionId: str) -> requests.Request:
        """
        :param transactionId: A valid stock transaction id
        """
        return requests.Request(
            method='GET',
            url=f'/stock/transactions/{transactionId}',
        )


class STOCK_TRANSACTIONS_BY_TRANSACTIONID_UNDO:
    @classmethod
    def POST(cls, transactionId: str) -> requests.Request:
        """
        :param transactionId: A valid stock transaction id
        """
        return requests.Request(
            method='POST',
            url=f'/stock/transactions/{transactionId}/undo',
        )


class STOCK_BARCODES_EXTERNAL_LOOKUP_BY_BARCODE:
    @classmethod
    def GET(cls, barcode: str, add: bool=None) -> requests.Request:
        """
        :param barcode: The barcode to lookup up
        :param add: When true, the product is added to the database on a successful lookup and the new product id is in included in the response
        """
        return requests.Request(
            method='GET',
            url=f'/stock/barcodes/external-lookup/{barcode}',
            params={'add': add},
        )


class RECIPES_BY_RECIPEID_ADD_NOT_FULFILLED_PRODUCTS_TO_SHOPPINGLIST:
    Body = TypedDict('Body', excludedProductIds=List[int])
    @classmethod
    def POST(cls, recipeId: str, body: Body) -> requests.Request:
        """
        :param recipeId: A valid recipe id
        """
        return requests.Request(
            method='POST',
            url=f'/recipes/{recipeId}/add-not-fulfilled-products-to-shoppinglist',
            json=body,
        )


class RECIPES_BY_RECIPEID_FULFILLMENT:
    @classmethod
    def GET(cls, recipeId: str) -> requests.Request:
        """
        :param recipeId: A valid recipe id
        """
        return requests.Request(
            method='GET',
            url=f'/recipes/{recipeId}/fulfillment',
        )


class RECIPES_BY_RECIPEID_CONSUME:
    @classmethod
    def POST(cls, recipeId: str) -> requests.Request:
        """
        :param recipeId: A valid recipe id
        """
        return requests.Request(
            method='POST',
            url=f'/recipes/{recipeId}/consume',
        )


class RECIPES_FULFILLMENT:
    @classmethod
    def GET(cls, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/recipes/fulfillment',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class RECIPES_BY_RECIPEID_COPY:
    @classmethod
    def POST(cls, recipeId: int) -> requests.Request:
        """
        :param recipeId: A valid recipe id of the recipe to copy
        """
        return requests.Request(
            method='POST',
            url=f'/recipes/{recipeId}/copy',
        )


class CHORES:
    @classmethod
    def GET(cls, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/chores',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class CHORES_BY_CHOREID:
    @classmethod
    def GET(cls, choreId: int) -> requests.Request:
        """
        :param choreId: A valid chore id
        """
        return requests.Request(
            method='GET',
            url=f'/chores/{choreId}',
        )


class CHORES_BY_CHOREID_EXECUTE:
    Body = TypedDict('Body', tracked_time=str, done_by=int)
    @classmethod
    def POST(cls, choreId: int, body: Body) -> requests.Request:
        """
        :param choreId: A valid chore id
        """
        return requests.Request(
            method='POST',
            url=f'/chores/{choreId}/execute',
            json=body,
        )


class CHORES_EXECUTIONS_BY_EXECUTIONID_UNDO:
    @classmethod
    def POST(cls, executionId: int) -> requests.Request:
        """
        :param executionId: A valid chore execution id
        """
        return requests.Request(
            method='POST',
            url=f'/chores/executions/{executionId}/undo',
        )


class CHORES_EXECUTIONS_CALCULATE_NEXT_ASSIGNMENTS:
    Body = TypedDict('Body', chore_id=int)
    @classmethod
    def POST(cls, body: Body) -> requests.Request:
        return requests.Request(
            method='POST',
            url=f'/chores/executions/calculate-next-assignments',
            json=body,
        )


class CHORES_BY_CHOREID_PRINTLABEL:
    @classmethod
    def GET(cls, choreId: int) -> requests.Request:
        """
        :param choreId: A valid chore id
        """
        return requests.Request(
            method='GET',
            url=f'/chores/{choreId}/printlabel',
        )


class CHORES_BY_CHOREIDTOKEEP_MERGE_BY_CHOREIDTOREMOVE:
    @classmethod
    def POST(cls, choreIdToKeep: int, choreIdToRemove: int) -> requests.Request:
        """
        :param choreIdToKeep: A valid chore id of the chore to keep
        :param choreIdToRemove: A valid chore id of the chore to remove
        """
        return requests.Request(
            method='POST',
            url=f'/chores/{choreIdToKeep}/merge/{choreIdToRemove}',
        )


class BATTERIES:
    @classmethod
    def GET(cls, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/batteries',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class BATTERIES_BY_BATTERYID:
    @classmethod
    def GET(cls, batteryId: int) -> requests.Request:
        """
        :param batteryId: A valid battery id
        """
        return requests.Request(
            method='GET',
            url=f'/batteries/{batteryId}',
        )


class BATTERIES_BY_BATTERYID_CHARGE:
    Body = TypedDict('Body', tracked_time=str)
    @classmethod
    def POST(cls, batteryId: int, body: Body) -> requests.Request:
        """
        :param batteryId: A valid battery id
        """
        return requests.Request(
            method='POST',
            url=f'/batteries/{batteryId}/charge',
            json=body,
        )


class BATTERIES_CHARGE_CYCLES_BY_CHARGECYCLEID_UNDO:
    @classmethod
    def POST(cls, chargeCycleId: int) -> requests.Request:
        """
        :param chargeCycleId: A valid charge cycle id
        """
        return requests.Request(
            method='POST',
            url=f'/batteries/charge-cycles/{chargeCycleId}/undo',
        )


class BATTERIES_BY_BATTERYID_PRINTLABEL:
    @classmethod
    def GET(cls, batteryId: int) -> requests.Request:
        """
        :param batteryId: A valid battery id
        """
        return requests.Request(
            method='GET',
            url=f'/batteries/{batteryId}/printlabel',
        )


class TASKS:
    @classmethod
    def GET(cls, query: List[str]=None, order: str=None, limit: int=None, offset: int=None) -> requests.Request:
        """
        :param query: An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for
        :param order: A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted)
        :param limit: The maximum number of objects to return
        :param offset: The number of objects to skip
        """
        return requests.Request(
            method='GET',
            url=f'/tasks',
            params={'query[]': query, 'order': order, 'limit': limit, 'offset': offset},
        )


class TASKS_BY_TASKID_COMPLETE:
    Body = TypedDict('Body', done_time=str)
    @classmethod
    def POST(cls, taskId: int, body: Body) -> requests.Request:
        """
        :param taskId: A valid task id
        """
        return requests.Request(
            method='POST',
            url=f'/tasks/{taskId}/complete',
            json=body,
        )


class TASKS_BY_TASKID_UNDO:
    @classmethod
    def POST(cls, taskId: int) -> requests.Request:
        """
        :param taskId: A valid task id
        """
        return requests.Request(
            method='POST',
            url=f'/tasks/{taskId}/undo',
        )


class CALENDAR_ICAL:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/calendar/ical',
        )


class CALENDAR_ICAL_SHARING_LINK:
    @classmethod
    def GET(cls) -> requests.Request:
        return requests.Request(
            method='GET',
            url=f'/calendar/ical/sharing-link',
        )


class PRINT_SHOPPINGLIST_THERMAL:
    @classmethod
    def GET(cls, list: int=1, printHeader: bool=True) -> requests.Request:
        """
        :param list: Shopping list id
        :param printHeader: Prints grocy logo if true
        """
        return requests.Request(
            method='GET',
            url=f'/print/shoppinglist/thermal',
            params={'list': list, 'printHeader': printHeader},
        )


from flask import render_template
from quanlynhasach import app


@app.route("/")
def index():
    categories=[{
        "id": 1,
        "name": "Sách"

    }, {
        "id": 2,
        "name": "quản lý nhân viên"

    }, {
        "id": 3,
        "name": "thống kê"

    }]



    products = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
            "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "Galaxy S22",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 5,
        "name": "Galaxy S23",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }]


    return render_template("index.html", categories= categories, products= products)


@app.route("/products/<int:product_id>")
def details(product_id):
    products = {
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }

    return render_template("details.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
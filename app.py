import requests
from bs4 import BeautifulSoup

#URL = 'https://www.amazon.in/Samsung-Galaxy-Prime-Light-128GB/dp/B0BD3V985M/ref=pd_rhf_d_se_s_pd_sbs_rvi_sccl_1_1/260-6174027-3410646?pd_rd_w=qsWzf&content-id=amzn1.sym.0d5f32d5-d8bf-40fc-9298-1b7e0b0b5c8d&pf_rd_p=0d5f32d5-d8bf-40fc-9298-1b7e0b0b5c8d&pf_rd_r=6WQ7N89BXMGPM6RYYWCP&pd_rd_wg=1AAfH&pd_rd_r=a6729b31-6a4b-46bf-ad6b-bba1bdb356ad&pd_rd_i=B0BD3V985M&th=1'

#URL = 'https://www.amazon.in/Oppo-Mystery-Storage-Additional-Exchange/dp/B08444S68L/ref=sr_1_1?crid=AVW82QK3GY0O&keywords=oppo&qid=1667829384&qu=eyJxc2MiOiI2LjI2IiwicXNhIjoiNS41OSIsInFzcCI6IjQuNDEifQ%3D%3D&s=electronics&sprefix=oppo%2Celectronics%2C518&sr=1-1'

products_to_track = [
    {
        "product_url":"https://www.amazon.in/Redmi-Note-Aqua-Green-Storage/dp/B08695YMYC/ref=sr_1_1?crid=29LNVXVE06A4C&keywords=redmi+note+9&qid=1667830202&qu=eyJxc2MiOiI1Ljc4IiwicXNhIjoiNS44NiIsInFzcCI6IjQuOTUifQ%3D%3D&s=electronics&sprefix=redmi+note+9%2Celectronics%2C243&sr=1-1",
         "name":"Redmi Note9",
        "target_price": 12000
    },
    {
        "product_url":"https://www.amazon.in/Vivo-Midnight-Additional-Exchange-Offers/dp/B07WHPXV46/ref=sr_1_1_sspa?keywords=vivo+y21&qid=1667830391&qu=eyJxc2MiOiI0LjQ1IiwicXNhIjoiMy41NSIsInFzcCI6IjIuOTgifQ%3D%3D&s=electronics&sprefix=vivo%2Celectronics%2C373&sr=1-1-spons&psc=1",
        "name":"Vivo Y21G",
        "target_price": 13000
    },
    {
        "product_url":"https://www.amazon.in/Samsung-Mystique-Storage-Purchased-Separately/dp/B09XJ48QPR/ref=sr_1_1_sspa?crid=3JCAUGORAX8Z6&keywords=samsung+mobile&qid=1667830526&qu=eyJxc2MiOiI2LjczIiwicXNhIjoiNi4xNyIsInFzcCI6IjQuODAifQ%3D%3D&s=electronics&sprefix=s%2Celectronics%2C256&sr=1-1-spons&psc=1",
        "name":"Samsung Galaxy M53 5G",
        "target_price": 28000
    },{

        "product_url":"https://www.amazon.in/Apple-iPhone-13-Mini-256GB/dp/B09G99CW2C/ref=sr_1_1?crid=32Y1XJAV4AGYA&keywords=apple+pho&qid=1667893023&qu=eyJxc2MiOiI0LjQ5IiwicXNhIjoiMS45MiIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=apple+pho%2Caps%2C253&sr=8-1",
        "name":"Apple iPhone 13 Mini",
        "target_price": 68000
    },
{
        "product_url":"https://www.amazon.in/Samsung-Galaxy-Cloud-128GB-Storage/dp/B08VB2MRF8/ref=sr_1_5?crid=M3OBADNPJBI6&keywords=samsung&qid=1667893228&qu=eyJxc2MiOiI2LjUzIiwicXNhIjoiNi4wOSIsInFzcCI6IjQuNDgifQ%3D%3D&sprefix=samsung+%2Caps%2C261&sr=8-5",
        "name":"Samsung Galaxy S20 FE",
        "target_price": 34000
    }

]

def give_product_price(URL):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(class_="a-offscreen")
    if (product_price ==None):
        product_price = soup.find(class_="a-offscreen-ourprice")

    return product_price.getText()

result_file = open('my_result_file.text','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' - \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()





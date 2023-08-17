import unittest
import allure
import json
import asyncio
import aiohttp

class PutCustomerData(unittest.TestCase):

    async def async_fetch_url(self, session, url):
            async with session.get(url) as response:
                return await response.text()

    async def async_modify_data(self, session, url, modified_json):
        async with session.put(url, data=modified_json) as response:
            return await response.text()

    async def test_put_customer_data_on_server(self):
        api_url = "http://localhost:5000/api/customers"

        async with aiohttp.ClientSession() as session:
            response_text = await self.async_fetch_url(session, api_url)

            json_data = json.loads(response_text)

            self.assertEqual(json_data["salary"], 3333)
            self.assertEqual(json_data["amount"], 100)
            self.assertEqual(json_data["percentage"], 0.03)

            updates = { "amount": 200, "percentage": 0.10}
            for key in updates:
                if key == "amount":
                    json_data["percentage"] = json_data[key] / json_data["salary"]
                else:
                    if key == "percentage":
                        json_data["amount"] = json_data[key] * json_data["salary"]   
                 
                modified_json = json.dumps(json_data, indent=4)

                await self.async_modify_data(session, api_url, modified_json)

                response_text_returned = await self.async_fetch_url(session, api_url)
                json_data_returned = json.loads(response_text_returned)

                self.assertEqual(json_data_returned, json_data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    unittest.main()
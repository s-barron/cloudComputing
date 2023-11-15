import requests
import json
import time

subscriptionId = "149a8005-b8f1-46e2-9798-cdf6d646c58f"
bearer = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAwNTkzOTUsIm5iZiI6MTcwMDA1OTM5NSwiZXhwIjoxNzAwMDYzNTk2LCJhY3IiOiIxIiwiYWlvIjoiQVRRQXkvOFZBQUFBNHM0WXdnTndGbklUN2lVL0hiTWI0b1V6czgyRENFLzVCQytOT2pYem9lV2wrcHliVDEyTXNHRnhxak1MQVFpdyIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiIxOGZiY2ExNi0yMjI0LTQ1ZjYtODViMC1mN2JmMmIzOWIzZjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkJhcnJvbiIsImdpdmVuX25hbWUiOiJTYXJhaCIsImdyb3VwcyI6WyI4MTA4YzUwMy1kNjU2LTQyY2YtOGVlNC04OTQ0YWVmMGZhZGUiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCIzZTg0ODA5OC1iNGExLTQxN2QtYTFiYS1jOWNmM2ZjZTlmNTEiLCI4MzhhMjg5YS04NGE0LTRjYTgtYWVlYy1iMzFlYzFkNzFkNGEiLCI0ZGMwM2I5Zi0xYjZjLTQ0MTUtYWMwNS04MjQyNzEzYzc1MjAiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ3LjI1Mi4xOS4xODEiLCJuYW1lIjoiQzIxNDE1OTA0IFNhcmFoIEJhcnJvbiIsIm9pZCI6IjBiMTBiZjM1LTE0MTMtNDFlZS1hYTNjLWIwZjIwNGYxZWFkMyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQ0NDM2IiwicHVpZCI6IjEwMDMyMDAxODMxRUNENjMiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QUZVLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Im5TYy1iNXhzSWdWLWpoZVVJaVVqSlBWOUhpazUtclhOd05wbl9OZWNxSHMiLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTQxNTkwNEBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxNDE1OTA0QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJ4bkMybzZ6d0JVeWxvWjZQdTJXekFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.ib_BV6F5qlZb4AKXR3xvFbSNrjMMf7pu9ibHcJV9qp1Liv6RWmfqVKyobAwLwn4N6xCAEVE2TBxTZvwU-D37XM0y5nKjh8MSxqDFoGM9zBtNses42dOVaXfJLf8mWHm9xNYjBkk9pgLpC40JIuarCUXlfx-UfPT80OULocU58mGQ9byhkPnVUPHJrnDQYtvjwZamzoX0LeHvtzOhgGWhw_5S06-p1pWFBcxawWnpEQkFRnlj3KQjeipjte4V6lZo2X6ToKpUnWNZs3Ojc3LNtqlMNJER4xZ-oJ0gRJX5gm2sOfdiQqx4bO91m_Revo0-P2idbgZhtdBLlZlXtnQkFQ"

defaultUrl = f"https://management.azure.com/subscriptions/{subscriptionId}/"

resourceGroupName = "lab4py"
virtualNetworkName= "net4py"
subnetName= "snet4py"
ipName = "ip4py"
vmName = "vm4py"
apiVersion = "2021-04-01"

def sendHttpRequest(url, json_data, headers):
    # Sending the POST request with the JSON payload
    response = requests.put(url, data=json_data, headers=headers)

    # Checks for answer
    if response.status_code == 200 or response.status_code == 201:
        print("Successful request")
        response_data = response.json()
        print("Response Data:", response_data)
    else:
        print(f"Error Request. Statuscode: {response.status_code}")

def createResourceGroup():
    global json_data, headers
    # create Resourcegroup
    urlCreateResourceGroup = f"{defaultUrl}resourcegroups/{resourceGroupName}?api-version={apiVersion}"
    # JSON-Data, that you want to send
    createResourceGroupPayloadData = {
        "location": "westeurope"
    }
    # converts Python data to JSON
    json_data = json.dumps(createResourceGroupPayloadData)
    # Set the HTTP headers to set the content type to JSON
    headers = {"Authorization": f"Bearer {bearer}",
               'Content-Type': 'application/json'}
    sendHttpRequest(urlCreateResourceGroup, json_data, headers)

def createVirtualNetwork():
    global json_data
    # create virtual network
    urlCreateVirtualNetwork = f"{defaultUrl}resourcegroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}?api-version=2023-05-01"
    payloadDataCreateVirtualNetwork = {
        "properties": {
            "addressSpace": {
                "addressPrefixes": [
                    "10.0.0.0/16"
                ]
            },
            "flowTimeoutInMinutes": 10
        },
        "location": "westeurope"
    }
    json_data = json.dumps(payloadDataCreateVirtualNetwork)
    sendHttpRequest(urlCreateVirtualNetwork, json_data, headers)

def createSubnet():
    global json_data
    # create subnet
    urlCreateSubnet = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}?api-version=2023-05-01"
    payloadDataCreateSubnet = {
        "properties": {
            "addressPrefix": "10.0.0.0/16"
        }
    }
    json_data = json.dumps(payloadDataCreateSubnet)
    sendHttpRequest(urlCreateSubnet, json_data, headers)

def createPublicIpAdress():
    global json_data
    # create public ip adress
    urlCreatePublicIPAdress = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{ipName}?api-version=2023-05-01"
    payloadDataCreatePublicIpAdress = {
        "location": "westeurope"
    }
    json_data = json.dumps(payloadDataCreatePublicIpAdress)
    sendHttpRequest(urlCreatePublicIPAdress, json_data, headers)

def createNetworkInterface():
    global networkInterfaceName, json_data
    # create network interface
    networkInterfaceName = "nic4py"
    urlCreateNetworkInterface = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}?api-version=2023-05-01"
    payloadDataCreateNetworkInterface = {
        "location": "westeurope",
        "properties": {
            "ipConfigurations": [
                {
                    "name": "ipconfig1",
                    "properties": {
                        "publicIPAddress": {
                            "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{ipName}"
                        },
                        "subnet": {
                            "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}"
                        }
                    }
                }
            ]
        },
        
    }
    json_data = json.dumps(payloadDataCreateNetworkInterface)
    sendHttpRequest(urlCreateNetworkInterface, json_data, headers)

def createVm():
    global json_data
    # create VM
    urlCreateVM = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}?api-version=2023-07-01"
    payloadDataCreateVM = {
        "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}",
        "type": "Microsoft.Compute/virtualMachines",
        "location": "westeurope",
        "properties": {
            "osProfile": {
                "adminUsername": "sarah",
                "secrets": [

                ],
                "computerName": f"{vmName}",
                "linuxConfiguration": {
                    "ssh": {
                        "publicKeys": [
                            {
                                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNSDv8HbW4Vmt6jifTdpVR5FUuhVOrqPqgK1NrSOLky0UI5ucJIZM6grBBCW6gETo/W8mc/gxbtV7lG/yX2ncvM7/eJvXVHM/AohdjpT/3EypANE/kYzoU0W6Qb8kmpGBpmeAWRpPPYyu4LOg5wnzIl5hg6088RihB+7uFDYeYu15odWxqKRgt5DHo2p2H4hDRBoi1IMhi1iU4SJ6fU4RzWTG6+xwDdNw8UzD3qamW7yH5v5gG7qx4p1gk2uM8E+4ZeiWdyVCsoung9HRNc1oRxNRoVtxcaFLIO5VyJ+p5X1aZMnkfckbcGwPRD97vGopcIBb//rRocAP2BOAdlktyHKPrXKYwoFrWVrHW6rrZj/aW8U+M81Xu01rXhnXMiKP8q6des/73l8Ug/rOZ1wqbePUvq61yQjsOtks7hKZFjdp9w4wqZ/krG130SFZrZ145rCn3JgfIcnDyxcrAGwBZRm4TQwthde/Jkxtp60k2vZjIPW9eOsr+onQ+Uu9PuVk= azureuser@cloudCompVm",       
                                "path": "/home/sarah/.ssh/authorized_keys",                  
                            }
                        ]
                    },
                    "disablePasswordAuthentication": True
                }
            },
            "networkProfile": {
                "networkInterfaces": [
                    {
                        "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}",
                        "properties": {
                            "primary": True
                        }
                    }
                ]
            },
            "storageProfile": {
                "imageReference": {
                    "sku": "16.04-LTS",
                    "publisher": "Canonical",
                    "version": "latest",
                    "offer": "UbuntuServer"
                },
                "dataDisks": [

                ]
            },
            "hardwareProfile": {
                "vmSize": "Standard_D1_v2"
            },
            "provisioningState": "Creating"
        }
        #"name": f"{vmName}"
    }
    json_data = json.dumps(payloadDataCreateVM)
    sendHttpRequest(urlCreateVM, json_data, headers)

createResourceGroup()
time.sleep(5)
createVirtualNetwork()
time.sleep(5)
createSubnet()
time.sleep(5)
createPublicIpAdress()
time.sleep(20)
createNetworkInterface()
time.sleep(10)
createVm()

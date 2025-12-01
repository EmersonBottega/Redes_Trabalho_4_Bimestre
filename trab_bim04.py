# Trabalho 04, from Emerson Bottega

# Cria a máscara como array
def create_mask(mask):
    mask_array = [0, 0, 0, 0]
    bits = int(mask)

    for i in range(4):
        if bits >= 8:
            mask_array[i] = 255
            bits -= 8
        else:
            mask_array[i] = (256 - 2**(8 - bits)) % 256
            bits = 0

    return mask_array

# Calcula rede fazendo com AND mascára + IP
def create_network(ip_arr, mask_arr):
    return [
        ip_arr[0] & mask_arr[0],
        ip_arr[1] & mask_arr[1],
        ip_arr[2] & mask_arr[2],
        ip_arr[3] & mask_arr[3]
    ]

# Calcula broadcast substituindo bits de host por 255
def create_broadcast(network, mask):
    return [
        network[0] + (255 - mask[0]),
        network[1] + (255 - mask[1]),
        network[2] + (255 - mask[2]),
        network[3] + (255 - mask[3])
    ]

# Calcula o primeiro ip de host
def create_fisrt_host_ip_adress(network):
    first = network.copy()
    first[3] += 1
    return first

# Calcula o último ip de host
def create_last_host_ip_adress(broadcast):
    last = broadcast.copy()
    last[3] -= 1
    return last

# Transformar array em string
def ip_array_to_string(arr):
    return ".".join(map(str, arr))

# Mostra a saída
def show_results(network, broadcast, first_ip_adress, last_ip_adress):
    print(f"Rede: {ip_array_to_string(network)}")
    print(f"Broadcast: {ip_array_to_string(broadcast)}")
    print(f"Hosts: de {ip_array_to_string(first_ip_adress)} a {ip_array_to_string(last_ip_adress)}")

# Início da aplicação
ip_input = input("Digite o IP/Máscara (ex: 192.168.10.50/24): \n")

splited_input = ip_input.split("/")
ip = splited_input[0]
ip_array = list(map(int, ip.split(".")))  # Converte "192.168.10.50" em array [192,168,10,50]

mask = splited_input[1]
mask_array = create_mask(mask)

network = create_network(ip_array, mask_array)
broadcast = create_broadcast(network, mask_array)
first_ip_adress = create_fisrt_host_ip_adress(network)
last_ip_adress = create_last_host_ip_adress(broadcast)

print("########################################")
show_results(network, broadcast, first_ip_adress, last_ip_adress)
print("########################################")
from math import log2
def build_huffman_tree(frequencies, q=4):
    # Создаем список узлов [частота, [символ, код]]
    nodes = [[freq, [symbol, ""]] for symbol, freq in frequencies.items()]

    n = len(nodes)
    if n % (q - 1) == 1:
        first_group_size = q
    elif n % (q - 1) == 0:
        first_group_size = q - 1
    else:
        first_group_size = n % (q - 1)
    
    while len(nodes) > 1:
        # Сортируем узлы по частоте (по возрастанию)
        nodes.sort(key=lambda x: x[0])
        
        # Определяем количество узлов для текущего объединения
        if len(nodes) == n:
            group_size = first_group_size
        else:
            group_size = q
        
        
        # Берем group_size узлов с наименьшими частотами
        group = [nodes.pop(0) for i in range(group_size)]
        
        # Добавляем '0', '1', '2', '3' к кодам узлов (суффиксы)
        for i, node in enumerate(group):
            for pair in node[1:]:
                pair[1] = pair[1] + str(i)  # Добавляем '0', '1', '2' или '3'
        
        # Создаем новый узел
        new_freq = sum(node[0] for node in group)
        new_symbols = []
        for node in group:
            new_symbols.extend(node[1:])
        new_node = [new_freq] + new_symbols
        
    
        nodes.append(new_node)
    
    
    return nodes[0]

# Функция для получения кодов Хаффмана
def get_huffman_codes(tree):
    codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        codes[symbol] = code
    return codes

# Функция для расчета средней длины кода
def calculate_average_length(codes, frequencies, total):
    avg_length = 0
    for symbol, code in codes.items():
        avg_length += len(code) * (frequencies[symbol] / total)
    return avg_length
#Функция для подсчета энтропии
def calculate_entropy(frequencies,total):
    entropy = 0
    for symbol in frequencies.keys():
        if frequencies[symbol] != 0:
            entropy -= frequencies[symbol]/total * log2(frequencies[symbol]/total)
    return entropy
s = 'ДОЛОХОВ БЫЛ ЧЕЛОВЕК СРЕДНЕГО РОСТА КУРЧАВЫЙ И С СВЕТЛЫМИ ГОЛУБЫМИ ГЛАЗАМИ ЕМУ БЫЛО ЛЕТ ДВАДЦАТЬ ПЯТЬ ОН НЕ НОСИЛ УСОВ КАК И ВСЕ ПЕХОТНЫЕ ОФИЦЕРЫ И РОТ ЕГО САМАЯ ПОРАЗИТЕЛЬНАЯ ЧЕРТА ЕГО ЛИЦА БЫЛ ВЕСЬ ВИДЕН ЛИНИИ ЭТОГО РТА БЫЛИ ЗАМЕЧАТЕЛЬНО ТОНКО ИЗОГНУТЫ В СРЕДИНЕ ВЕРХНЯЯ ГУБА ЭНЕРГИЧЕСКИ ОПУСКАЛАСЬ НА КРЕПКУЮ НИЖНЮЮ ОСТРЫМ КЛИНОМ И В УГЛАХ ОБРАЗОВЫВАЛОСЬ ПОСТОЯННО ЧТО ТО ВРОДЕ ДВУХ УЛЫБОК ПО ОДНОЙ С КАЖДОЙ СТОРОНЫ И ВСЕ ВМЕСТЕ А ОСОБЕННО В СОЕДИНЕНИИ С ТВЕРДЫМ НАГЛЫМ УМНЫМ ВЗГЛЯДОМ СОСТАВЛЯЛО ВПЕЧАТЛЕНИЕ ТАКОЕ ЧТО НЕЛЬЗЯ БЫЛО НЕ ЗАМЕТИТЬ ЭТОГО ЛИЦА ДОЛОХОВ БЫЛ НЕБОГАТЫЙ ЧЕЛОВЕК БЕЗ ВСЯКИХ СВЯЗЕЙ И НЕСМОТРЯ НА ТО ЧТО АНАТОЛЬ ПРОЖИВАЛ ДЕСЯТКИ ТЫСЯЧ ДОЛОХОВ ЖИЛ С НИМ И УСПЕЛ СЕБЯ ПОСТАВИТЬ ТАК ЧТО АНАТОЛЬ И ВСЕ ЗНАВШИЕ ИХ УВАЖАЛИ ДОЛОХОВА БОЛЬШЕ ЧЕМ АНАТОЛЯ'
alph = {' ': 0,
        'А': 0,
        'Б': 0,
        'В': 0,
        'Г': 0,
        'Д': 0,
        'Е': 0,
        'Ж': 0,
        'З': 0,
        'И': 0,
        'Й': 0,
        'К': 0,
        'Л': 0,
        'М': 0,
        'Н': 0,
        'О': 0,
        'П': 0,
        'Р': 0,
        'С': 0,
        'Т': 0,
        'У': 0,
        'Ф': 0,
        'Х': 0,
        'Ц': 0,
        'Ч': 0,
        'Ш': 0,
        'Щ': 0,
        'Ъ': 0,
        'Ы': 0,
        'Ь': 0,
        'Э': 0,
        'Ю': 0,
        'Я': 0
        }

total = 0
for i in s:
    alph[i] += 1
    total += 1

# Построение дерева Хаффмана
tree = build_huffman_tree(alph)

# Получение кодов Хаффмана
codes = get_huffman_codes(tree)

# Расчет средней длины кода
avg_length = calculate_average_length(codes, alph, total)


entropy = calculate_entropy(alph,total)

# Расчет избыточности
otvet = avg_length - entropy

print("Коды Хаффмана:")
for symbol, code in codes.items():
    print(f"{symbol}: {code}")

print(f"\nСредняя длина кода: {avg_length} ")
print(f"Энтропия: {entropy}")
print(f"Избыточность: {otvet}")

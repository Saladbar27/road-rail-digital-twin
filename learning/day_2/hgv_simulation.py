
num_hgv = int(input('Enter the number of HGVs.'))

for num in range(1, num_hgv + 1):
    print(f'HGV {num}')

    if num % 3 == 0:
        print('Signal: None')
        print('Status: Waiting')
        
    else:
        print('Signal: Good')
        print('Status: Moving')
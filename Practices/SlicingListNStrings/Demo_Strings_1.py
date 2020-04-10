#!/usr/bin/env python3

sample_url = 'https://www.google.co.in'

print(sample_url)

#reverse the string
print(f'{sample_url[::-1]}')

#print top level domain
print(f'{sample_url[-5:]}')

#Print URL whithout the https://
print(f'{sample_url[8:]}')

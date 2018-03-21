a = [0,0,0]
m_sum = -1
tmp = 0
b = 0
c = 0
for i in range(3):
    a[i] = int(input())
for i in range(3):
    b = (i+1)%3
    c = (i+2)%3
    tmp = 2*abs(b-i)*a[b] + 2*abs(c-i)*a[c]
    if m_sum == -1 or tmp < m_sum:
        m_sum = tmp
print(m_sum)

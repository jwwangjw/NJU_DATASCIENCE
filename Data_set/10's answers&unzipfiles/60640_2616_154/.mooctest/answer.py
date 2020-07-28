for _ in range(int(input())):
    a, b = map( int, input().split() )
    print( 1 if ( ( b * ( b + 1 ) ) / 2 ) <= a else 0 )
def solution(chicken):
    coupon = chicken
    service = 0

    while coupon >= 10:
        new = coupon // 10
        service += new
        coupon = new + (coupon % 10)  # 남은 쿠폰 + 새로 받은 치킨의 쿠폰

    return service
raw_data = " eMP-001; nguyen van a ;0987654321; sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van c ;0988abc123 ; IT "

while True:
    print("\n===== MENU =====")
    print("1. Hiển thị dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo ID")
    print("4. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)
    
    if choice == 1:
        print("\n=== DỮ LIỆU GỐC ===")
        print(raw_data)

    elif choice == 2:
        print("\n=== BÁO CÁO NHÂN VIÊN ===")
        print(f"{'ID':<12}{'HỌ TÊN':<20}{'SĐT':<20}{'PHÒNG BAN'}")
        print("-" * 65)

        employees = raw_data.split("|")

        for employee in employees:
            fields = employee.split(";")

            if len(fields) != 4:
                continue

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip()
            department = fields[3].strip().upper()

            phone = phone.replace("-", "")

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(
                f"{emp_id:<12}"
                f"{name:<20}"
                f"{phone:<20}"
                f"{department}"
            )

    elif choice == 3:
        keyword = input("Nhập mã nhân viên: ").strip().upper()

        employees = raw_data.split("|")
        found = False

        for employee in employees:
            fields = employee.split(";")

            if len(fields) != 4:
                continue

            emp_id = fields[0].strip().upper()
            name = fields[1].strip().title()
            phone = fields[2].strip()
            department = fields[3].strip().upper()

            phone = phone.replace("-", "")

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            if emp_id == keyword:
                print("\n=== THÔNG TIN NHÂN VIÊN ===")
                print("ID:", emp_id)
                print("Họ tên:", name)
                print("SĐT:", phone)
                print("Phòng ban:", department)
                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == 4:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
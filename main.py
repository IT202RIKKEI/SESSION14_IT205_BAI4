student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

# hàm set rank
def set_rank(avg_score:float)-> str:
    if avg_score >= 8:
        return "Giỏi"
    elif avg_score >= 6.5:
        return "Khá"
    elif avg_score >= 5:
        return "Trung bình"
    else:
        return "Yếu (Cảnh báo đỏ)"
# *** Chức năng 1: Xem bảng điểm và học lực
def display_grades(records:list)-> str:
    
    
    
    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for position, record in enumerate(records, start=1):
        # tính điểm trung bình
        avg_score = (record["math"] + record["physics"] + record["chemistry"]) / 3
        rank = set_rank(avg_score)
        
        print(f"{position}. [{record['student_id']}] {record['name']} | {record['math']} | {record['physics']} | {record['chemistry']} | ĐTB: {avg_score:.2f} - {rank}")
# *** Chức năng 2: Cập nhật điểm thi sinh viên
def update_student_score(student_records:list):
    
    update_student_id = input("Mời bạn nhập vào id cần cập nhật điểm: ").strip().upper()
    
    found_student_index = find_student_by_id(student_records, update_student_id)
    
    if found_student_index == -1:
        return
    
    # cập nhật điểm
    # nhập môn cần sửa
    while True:
        try:
            subject_choice = int(input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "))
            
            try:
                new_score = float(input("Nhập điểm mới (0-10): "))
                
                if new_score < 0 or new_score > 10:
                    print("Điểm không hợp lệ!")
                    return
                
            except ValueError:
                print("Không được nhậ khác kiểu dữ liệu")
                continue
            
            match subject_choice:
                case 1:
                    # sửa điểm toán
                    student_records[found_student_index]["math"] = new_score
                    print(
                        f">> Đã cập nhật điểm Toán của sinh viên "
                        f"'{student_records[found_student_index]['name']}' thành {new_score}."
                    )
                    return
                case 2:
                    # sửa điểm toán
                    student_records[found_student_index]["physics"] = new_score
                    print(
                        f">> Đã cập nhật điểm lý của sinh viên "
                        f"'{student_records[found_student_index]['name']}' thành {new_score}."
                    )
                    return
                case 3:
                    # sửa điểm toán
                    student_records[found_student_index]["chemistry"] = new_score
                    print(
                        f">> Đã cập nhật điểm hóa của sinh viên "
                        f"'{student_records[found_student_index]['name']}' thành {new_score}."
                    )
                    return
                case _:
                    print("Không có lựa chọn phù hợp")

        except ValueError:
            print("Nhập từ 1-3")
        
    

# def tìm học sinh trong list Dict trả về index
def find_student_by_id(student_records:list, student_id: str) -> int:
    
    for index,student in enumerate(student_records):
        if student_id == student["student_id"]:
            return index
    else:
        print(f"Không tìm thấy id: {student_id} ")
        return -1


# *** Chức năng 3: Báo cáo thống kê (Đỗ/Trượt)
def generate_report(student_records:list):
    
    total_student = len(student_records)
    if total_student == 0:
        print("Danh sách trống, không có dữ liệu để thống kê!")
        return
    
    passed = 0
    failed = 0
    
    for student in student_records:
        avg_score = (student["math"] + student["physics"] + student["chemistry"]) / 3
        
        if avg_score >= 5:
            passed += 1
        else:
            failed += 1
    
    total_passed_subject_percent = (passed / total_student) * 100
    total_failed_subject_percent = (failed / total_student) * 100
    
    print(f"Tổng số học sinh: {total_student}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên (chiếm {total_passed_subject_percent:.2f}%)")
    print(f"Số lượng rớt môn (ĐTB < 5.0): {failed} sinh viên (chiếm {total_failed_subject_percent:.2f}%)")
    
# *** Chức năng 4: Tìm sinh viên Thủ khoa
def find_valedictorian(records: list):
    if not records:
        print("Danh sách sinh viên trống!")
        return

    max_avg_score = -1
    valedictorian = None

    # Duyệt qua từng sinh viên để tìm điểm trung bình cao nhất
    for student in records:
        avg_score = (student["math"] + student["physics"] + student["chemistry"]) / 3
        
        # Nếu điểm TB hiện tại lớn hơn kỷ lục (max_avg_score)
        if avg_score > max_avg_score:
            max_avg_score = avg_score
            valedictorian = student # Lưu lại toàn bộ thông tin của thủ khoa

    # In ra màn hình vinh danh
    if valedictorian:
        print("\n--- VINH DANH THỦ KHOA ---")
        print(f" Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
        print(f" Điểm Trung Bình: {max_avg_score:.2f}")
        print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
        print("--------------------------\n")

while True:
    try:
        choice = int(input("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====

1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình

======================================================
Chọn chức năng (1-5): """))

        if choice < 1 or choice > 5:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-5!")
            continue

        match choice:

            case 1:
                display_grades(student_records)
            case 2:
                update_student_score(student_records)
            case 3:
                generate_report(student_records)
            case 4:
                find_valedictorian(student_records)

            case 5:
                print("Thoát chương trình thành công!")
                break

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


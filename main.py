student_records = [
    {"student_id": "SV001", "name": "Nguyễn Văn A", "math": 8.5, "physics": 7.0, "chemistry": 9.0},
    {"student_id": "SV002", "name": "Trần Thị B", "math": 4.0, "physics": 5.5, "chemistry": 5.0},
    {"student_id": "SV003", "name": "Lê Văn C", "math": 9.5, "physics": 9.0, "chemistry": 8.5}
]

# 1. Hàm tính điểm trung bình (Tách biệt logic)
def calculate_average(s):
    return (s["math"] + s["physics"] + s["chemistry"]) / 3

def set_rank(avg_score: float) -> str:
    if avg_score >= 8: return "Giỏi"
    elif avg_score >= 6.5: return "Khá"
    elif avg_score >= 5: return "Trung bình"
    else: return "Yếu (Cảnh báo đỏ)"

def find_student_by_id(records: list, student_id: str) -> int:
    # Chuẩn hóa ID ngay khi tìm kiếm
    search_id = student_id.strip().upper()
    for index, student in enumerate(records):
        if student["student_id"] == search_id:
            return index
    return -1

def display_grades(records: list):
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    for pos, r in enumerate(records, 1):
        avg = calculate_average(r)
        print(f"{pos}. [{r['student_id']}] {r['name']} | ĐTB: {avg:.2f} - {set_rank(avg)}")

def update_student_score(records: list):
    s_id = input("Nhập ID sinh viên cần sửa: ").strip().upper()
    idx = find_student_by_id(records, s_id)
    if idx == -1:
        print("Không tìm thấy sinh viên!")
        return
    
    subjects = {1: "math", 2: "physics", 3: "chemistry"}
    try:
        choice = int(input("Chọn môn (1-Toán, 2-Lý, 3-Hóa): "))
        if choice not in subjects:
            print("Lựa chọn không hợp lệ!")
            return
        
        new_score = float(input("Nhập điểm mới (0-10): "))
        if 0 <= new_score <= 10:
            records[idx][subjects[choice]] = new_score
            print("Cập nhật thành công!")
        else:
            print("Điểm không hợp lệ!")
    except ValueError:
        print("Dữ liệu nhập vào phải là số!")

def generate_report(records: list):
    if not records:
        print("Danh sách trống!")
        return
    passed = sum(1 for s in records if calculate_average(s) >= 5)
    total = len(records)
    print(f"Qua môn: {passed}/{total} ({passed/total*100:.2f}%)")

def find_valedictorian(records: list):
    if not records: return
    # Sử dụng hàm max với key là hàm calculate_average
    top_student = max(records, key=calculate_average)
    avg = calculate_average(top_student)
    print(f"\n--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {top_student['name']} | ĐTB: {avg:.2f}")

# Main menu
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI =====")
    print("1. Xem bảng điểm\n2. Cập nhật điểm\n3. Báo cáo\n4. Thủ khoa\n5. Thoát")
    try:
        choice = int(input("Chọn (1-5): "))
        if choice == 1: display_grades(student_records)
        elif choice == 2: update_student_score(student_records)
        elif choice == 3: generate_report(student_records)
        elif choice == 4: find_valedictorian(student_records)
        elif choice == 5: break
    except ValueError:
        print("Vui lòng nhập số!")
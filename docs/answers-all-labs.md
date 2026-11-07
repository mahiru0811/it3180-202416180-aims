# Tổng hợp Câu hỏi thảo luận từ Lab 01 đến Lab 05
**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm
**Dự án:** AIMS-mini

---

## LAB 01 – Thiết lập môi trường & Refactor flow

### 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ:** Cấu hình `--global` được lưu trong tệp `~/.gitconfig` (nằm ở thư mục gốc của người dùng hệ điều hành).
- **Sự khác biệt:**
  - `--global`: Áp dụng cho tất cả các kho lưu trữ (repository) của người dùng trên máy tính.
  - `--local`: Được lưu tại `.git/config` bên trong một repository cụ thể. Cấu hình local có mức ưu tiên cao hơn và sẽ ghi đè lên cấu hình global trong phạm vi repository đó.

### 2. Vì sao phải dùng `git mv` thay vì di chuyển tệp thủ công?
- `git mv` giúp Git nhận diện ngay lập tức thao tác đổi tên/di chuyển tệp (`renamed`) và đưa thẳng vào Staging area.
- Thao tác này bảo toàn lịch sử commit và siêu dữ liệu (metadata) của tệp (cho phép theo dõi xuyên suốt qua lệnh `git log --follow`), tránh việc Git hiểu nhầm thành hai hành vi rời rạc là xóa tệp cũ và tạo một tệp mới tinh.

### 3. Nhánh `release/lab01` có phải là baseline không?
- **Có.** `release/lab01` là một baseline cấu hình vì nó đại diện cho một trạng thái mã nguồn và tài liệu đã được kiểm thử, thống nhất và đóng băng tại thời điểm kết thúc bài thực hành số 1, dùng làm căn cứ bàn giao/nộp bài và đối chiếu cho các vòng phát triển sau.

### 4. Vì sao không commit thẳng lên `master` dù chỉ làm việc một mình?
- Nhằm tuân thủ nguyên tắc Kiểm soát thay đổi (Change Control) của SCM: mọi sửa đổi phải được cô lập trên nhánh riêng, có lý do rõ ràng và đi qua quy trình Pull Request.
- Giúp bảo vệ trạng thái ổn định của nhánh chính `master`, rèn luyện kỷ luật làm việc nhóm chuyên nghiệp và tránh rủi ro đưa mã lỗi trực tiếp vào baseline.

---

## LAB 02 – Feature/Topic flow & Pull Request

### 1. Vì sao phải đồng bộ `master` vào nhánh tính năng trước khi mở Pull Request?
- Để tích hợp sớm các thay đổi mới nhất đã có trên `master` vào nhánh tính năng cục bộ.
- Giúp phát hiện và giải quyết xung đột (merge conflicts) hoặc lỗi phá vỡ tương thích ngay tại máy lập trình viên trước khi đẩy lên remote và yêu cầu reviewer kiểm tra.

### 2. Khi nào không được phép rebase?
- Tuyệt đối không được `rebase` trên các nhánh công khai (public branch) hoặc các commit đã được chia sẻ/đẩy lên remote mà người khác đang cùng làm việc (như nhánh `master`, `release/*`).
- Lý do: `rebase` tính toán lại toàn bộ mã băm (SHA) và viết lại lịch sử commit, gây sai lệch và xung đột nghiêm trọng cho các thành viên khác trong nhóm.

### 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- `feature/*`: Dùng để phát triển các chức năng nghiệp vụ cụ thể của phần mềm (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- `topic/*`: Dùng cho các chủ đề công việc ngắn hạn không mang tính năng mã nguồn trực tiếp của ứng dụng (ví dụ: bổ sung cấu hình build, sửa PR template `topic/pr-template`, cập nhật tài liệu use case `topic/use-case-diagram`).

---

## LAB 03 – Bugfix flow, xung đột & hoàn tác

### 1. Merge base là gì?
- `Merge base` là commit tổ tiên chung gần nhất (common ancestor) giữa hai nhánh chuẩn bị hợp nhất với nhau.
- Git sử dụng commit này để thực hiện thuật toán hòa trộn 3 chiều (3-way merge) giữa merge base, đỉnh của nhánh hiện tại và đỉnh của nhánh cần gộp nhằm xác định các đoạn mã được chỉnh sửa độc lập hoặc có xung đột.

### 2. Vì sao trên nhánh `master` và `release/*` bắt buộc phải dùng `revert` thay vì `reset`?
- Các nhánh `master` và `release/*` là nhánh dùng chung đã được đẩy lên remote. Lệnh `reset` sẽ xóa bỏ commit cục bộ và đòi hỏi phải đẩy cưỡng bức (`--force`), phá vỡ chuỗi lịch sử của những người khác.
- `revert` không xóa lịch sử cũ mà tạo thêm một commit mới có nội dung đảo ngược hoàn toàn thay đổi trước đó, đảm bảo tính toàn vẹn và minh bạch cho công tác kiểm toán cấu hình.

---

## LAB 04 – Release flow & phiên bản phát hành

### 1. Vì sao nhánh `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.
- **Trong Release Flow:** `master` luôn là dòng phát triển chính liên tục (trunk-based). Nhánh `release/*` chỉ dùng để đóng băng sản phẩm nộp bài hoặc bảo trì bản phát hành. Nếu có lỗi phát sinh trên release, bản vá sẽ được lan truyền về `master` thông qua `cherry-pick`, tránh đưa các cấu hình riêng biệt của bản phát hành ngược lại `master`.
- **So sánh với GitFlow:** GitFlow duy trì song song hai nhánh sống vĩnh viễn (`master`/`main` và `develop`). Khi hoàn thành một phiên bản, GitFlow bắt buộc merge nhánh `release` vào cả `master` lẫn `develop`. Release Flow tinh gọn hơn, giảm thiểu xung đột nhánh và phù hợp với mô hình CI/CD hiện đại.

### 2. Vì sao đánh số phiên bản là `1.0.0` mà không phải `0.4.0`?
- Theo quy tắc Semantic Versioning (SemVer), tiền tố `0.y.z` dành cho giai đoạn phát triển ban đầu (initial development), khi API chưa ổn định.
- Phiên bản `1.0.0` đánh dấu baseline chính thức đầu tiên (first stable release/production ready), cam kết về tính ổn định của các chức năng nghiệp vụ và quy trình SCM đã hoàn chỉnh.

---

## LAB 05 – Hotfix flow & bảo trì nhiều phiên bản

### 1. Ưu và nhược điểm của Upstream First so với Release First?
- **Upstream First (sửa trên `master` trước rồi cherry-pick về `release/*`):**
  - *Ưu điểm:* Đảm bảo bản vá luôn có mặt trên dòng phát triển chính, không bao giờ bị quên đưa vào các bản phát hành tương lai.
  - *Nhược điểm:* Chậm trễ hơn trong việc phát hành bản vá khẩn cấp cho khách hàng đang gặp sự cố trên môi trường production.
- **Release First (sửa trên `release/*` trước rồi cherry-pick về `master`):**
  - *Ưu điểm:* Khắc phục và phát hành bản vá PATCH (v1.0.1) ngay lập tức cho người dùng bị ảnh hưởng.
  - *Nhược điểm:* Đòi hỏi quy trình kiểm toán cấu hình nghiêm ngặt; nếu quên lan truyền về `master`, lỗi sẽ tái phát (regression) ở các phiên bản tiếp theo.

### 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- Vòng lặp kiểm thử tự động trên cả 3 phiên bản sẽ in ra kết quả kiểm tra độ dài tìm kiếm:
  `v1.1.0: 0` thay vì `1` (do hàm tìm kiếm trên `release/lab05` vẫn phân biệt chữ hoa/thường).
- Lệnh truy vết cherry-pick:
  `git log origin/release/lab05 --grep "cherry picked from commit <FIX_SHA>"` sẽ trả về kết quả rỗng.

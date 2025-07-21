### Bài tập thực hành các hàm MySQL (Nâng cao với JOIN)

Dưới đây là 20 bài tập được thiết kế để thực hành các hàm trong MySQL. Nhiều bài tập yêu cầu phải **kết hợp (JOIN) các bảng** trước khi áp dụng hàm.

#### **Phần 1: Các hàm xử lý chuỗi (String Functions)**

**1. (`CONCAT` & `JOIN`) Tạo thông tin khách hàng:**

- Viết một truy vấn để hiển thị một cột duy nhất `customer_order_info` cho mỗi đơn hàng. Cột này chứa tên đầy đủ của khách hàng và `order_id`, theo định dạng: "Khách hàng: [Họ tên đầy đủ] - Đơn hàng: [ID đơn hàng]". (Ví dụ: "Khách hàng: Minh Nguyen - Đơn hàng: 1").
    

**2. (`UPPER`, `LOWER` & `JOIN`) Chuẩn hóa email của khách hàng có đơn hàng:**

- Viết một truy vấn để lấy ra địa chỉ email (viết bằng chữ thường) của tất cả các khách hàng đã từng đặt hàng sản phẩm thuộc danh mục 'Electronics' (`category_id` = 1).
    

**3. (`LENGTH` & `JOIN`) Tìm độ dài tên sản phẩm đã bán:**

- Viết một truy vấn để hiển thị tên của mỗi sản phẩm (`product_name`) và độ dài của tên đó, nhưng chỉ cho những sản phẩm đã được bán trong tháng 6 năm 2025.
    

**4. (`SUBSTRING` & `JOIN`) Tạo mã tham chiếu đơn hàng:**

- Viết một truy vấn để tạo một mã tham chiếu (`reference_code`) cho mỗi đơn hàng. Mã này được tạo bằng cách lấy 3 ký tự đầu của `last_name` của khách hàng (viết hoa), nối với `customer_id`, ký tự '-', và `order_id`. (Ví dụ: NGU1-1).
    

**5. (`TRIM`) Làm sạch dữ liệu (Giả định):**

- Giả sử cột `shipper_name` trong bảng `Shippers` có thể chứa khoảng trắng thừa. Viết một truy vấn để hiển thị tên các nhà vận chuyển (đã được làm sạch) đã giao các đơn hàng cho khách hàng có `customer_id` = 2.
    

#### **Phần 2: Các hàm xử lý ngày tháng (Date Functions)**

**6. (`DATE_FORMAT` & `JOIN`) Định dạng ngày tháng cho đơn hàng của khách hàng:**

- Viết một truy vấn để hiển thị tên khách hàng (`first_name`, `last_name`) và ngày đặt hàng (`order_date`) của họ, với ngày tháng được định dạng theo kiểu `Ngày dd, Tháng mm, Năm yyyy`.
    

**7. (`YEAR`, `MONTH`, `DAY` & `JOIN`) Phân tích ngày tuyển dụng của nhân viên:**

- Từ bảng `Employees`, viết một truy vấn hiển thị tên nhân viên và 3 cột riêng biệt cho năm, tháng, ngày họ được tuyển dụng (`hire_date`), chỉ cho những nhân viên đã xử lý ít nhất một đơn hàng.
    

**8. (`DATEDIFF` & `JOIN`) Tính thời gian giao hàng kèm tên nhà vận chuyển:**

- Viết một truy vấn để tính số ngày cần thiết để giao hàng cho mỗi đơn hàng. Kết quả cần hiển thị `order_id`, tên khách hàng (`first_name`), tên nhà vận chuyển (`shipper_name`), và số ngày chênh lệch giữa `shipped_date` và `order_date`.
    

**9. (`CURRENT_DATE` & `JOIN`) Tính thâm niên của khách hàng đã mua hàng:**

- Viết một truy vấn để tính xem mỗi khách hàng đã đăng ký được bao nhiêu ngày tính đến hôm nay. Chỉ hiển thị kết quả cho những khách hàng đã đặt ít nhất một đơn hàng.
    

**10. (`DATE_ADD` & `JOIN`) Xác định hạn chót trả hàng cho sản phẩm:** * Viết một truy vấn để hiển thị `order_id`, `product_name`, `order_date`, và ngày hết hạn trả hàng (sau 30 ngày kể từ `order_date`) cho tất cả các sản phẩm đã được bán.

**11. (`DAYOFWEEK` & `JOIN`) Tìm ngày đặt hàng phổ biến cho một danh mục:** * Viết một truy vấn để đếm xem có bao nhiêu đơn hàng cho danh mục 'Books' (`category_id` = 2) được đặt vào mỗi ngày trong tuần (1 = Chủ nhật, 2 = Thứ hai, ...).

**12. (`EXTRACT` & `JOIN`) Tìm doanh thu theo quý cho mỗi nhân viên:** * Viết một truy vấn để tính tổng doanh thu (`quantity` * `list_price`) cho mỗi nhân viên (`employee_id`, `first_name`) theo từng quý.

**13. (`LAST_DAY` & `JOIN`) Tìm ngày cuối tháng cho đơn hàng có sản phẩm cụ thể:** * Viết một truy vấn để hiển thị `order_id` và ngày cuối cùng của tháng đặt hàng cho tất cả các đơn hàng có chứa sản phẩm 'Laptop Dell XPS 15'.

#### **Phần 3: Các hàm tính toán và điều khiển**

**14. (`AVG`, `ROUND` & `JOIN`) Tính giá bán trung bình theo danh mục:** * Viết một truy vấn để tính giá bán trung bình của các sản phẩm cho mỗi danh mục (`category_name`). Làm tròn kết quả đến 2 chữ số thập phân.

**15. (`MAX`, `MIN` & `JOIN`) Tìm sản phẩm đắt nhất và rẻ nhất trong một đơn hàng:** * Đối với đơn hàng có `order_id` = 4, hãy viết truy vấn để tìm ra giá (`list_price`) cao nhất và giá thấp nhất của các sản phẩm trong đơn hàng đó.

**16. (`COALESCE` hoặc `IFNULL` & `JOIN`) Hiển thị trạng thái giao hàng của khách hàng:** * Viết một truy vấn để liệt kê tên đầy đủ của khách hàng, `order_id` của họ, và một cột `shipping_status` hiển thị `shipped_date` hoặc dòng chữ 'Chưa giao hàng' nếu `shipped_date` là `NULL`.

**17. (`GREATEST` & `JOIN`) So sánh giá sản phẩm:** * Đối với mỗi mục hàng trong bảng `Order_Items`, hãy hiển thị `order_id`, `product_name`, `list_price` (giá tại thời điểm mua) và `unit_price` (giá hiện tại). Thêm một cột `highest_price` để hiển thị giá nào cao hơn giữa hai giá đó.

**18. (`CONVERT` & `JOIN`) Chuyển đổi kiểu dữ liệu theo danh mục:** * Viết một truy vấn để hiển thị `product_name` và `unit_price` của các sản phẩm thuộc danh mục 'Clothing' (`category_id` = 4). Trong kết quả, hãy chuyển đổi cột `unit_price` sang kiểu `CHAR` và nối nó với chuỗi ' VND'.

**19. (`IFNULL` & `JOIN`) Hiển thị thông tin liên lạc của khách hàng theo nhà vận chuyển:** * Viết một truy vấn để hiển thị thông tin liên lạc ưu tiên (`phone_number` nếu có, nếu không thì dùng `email`) của tất cả các khách hàng đã sử dụng dịch vụ của 'Viettel Post' (`shipper_id` = 2).

**20. (Bài tập tổng hợp) Tạo báo cáo chi tiết đơn hàng:** * Viết một truy vấn duy nhất để tạo báo cáo cho tất cả các mục hàng đã đặt. Báo cáo cần các cột sau: `order_id`, `full_name` của khách hàng, `product_name`, `category_name`, `quantity`, tổng giá trị của mục hàng đó (`quantity` * `list_price`), và `order_date`.
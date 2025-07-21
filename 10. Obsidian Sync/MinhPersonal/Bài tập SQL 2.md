### Bài tập SQL nâng cao: Subquery, CTE, và CASE WHEN

Dưới đây là 10 bài tập được thiết kế để thực hành các kỹ thuật truy vấn nâng cao trong MySQL, sử dụng cơ sở dữ liệu `store_db`.

#### **Phần 1: Truy vấn con (Subquery)**

**1. (Subquery trong `WHERE`) Tìm khách hàng đã mua sản phẩm cụ thể:**

- Viết một truy vấn để tìm `first_name` và `last_name` của tất cả các khách hàng đã từng mua sản phẩm có tên là 'Smartphone Samsung Galaxy S25'.
    
- _Gợi ý: Bạn sẽ cần một truy vấn con để tìm tất cả các `order_id` có chứa sản phẩm này, sau đó một truy vấn con khác để tìm `customer_id` từ những đơn hàng đó._
    

**2. (Subquery trong `FROM`) Tìm nhân viên có tổng doanh thu cao nhất:**

- Viết một truy vấn để tìm ra nhân viên (`first_name`, `last_name`) đã tạo ra tổng doanh thu cao nhất.
    
- _Gợi ý: Tạo một truy vấn con để tính tổng doanh thu (`quantity` * `list_price`) cho mỗi `employee_id`. Sau đó, từ kết quả đó, tìm ra người có tổng doanh thu lớn nhất._
    

**3. (Subquery tương quan - Correlated Subquery) Tìm các đơn hàng có giá trị lớn hơn trung bình:**

- Viết một truy vấn để liệt kê tất cả các `order_id` có tổng giá trị lớn hơn giá trị trung bình của TẤT CẢ các đơn hàng.
    
- _Gợi ý: Đối với mỗi đơn hàng, bạn cần tính tổng giá trị của nó và so sánh với giá trị trung bình được tính từ một truy vấn con._
    

#### **Phần 2: Biểu thức bảng chung (Common Table Expression - CTE)**

**4. (CTE đơn giản) Liệt kê doanh thu theo từng danh mục sản phẩm:**

- Sử dụng CTE, viết một truy vấn để tính tổng doanh thu cho mỗi danh mục sản phẩm (`category_name`). Báo cáo cần hiển thị tên danh mục và tổng doanh thu tương ứng, sắp xếp theo doanh thu giảm dần.
    
- _Gợi ý: CTE đầu tiên có thể nối `Products` và `Order_Items` để lấy `category_id` và doanh thu cho mỗi mục hàng. Truy vấn cuối cùng sẽ nhóm kết quả đó và nối với `Categories` để lấy tên._
    

**5. (CTE đa bước) Tìm khách hàng chi tiêu nhiều nhất trong Quý 3 năm 2025:**

- Sử dụng hai CTE, hãy tìm ra khách hàng (`first_name`, `last_name`) có tổng chi tiêu cao nhất trong Quý 3 năm 2025 (tháng 7, 8, 9).
    
- _Gợi ý:_
    
    - `CTE 1`: Lọc ra các đơn hàng trong Quý 3 và tính tổng giá trị cho mỗi đơn hàng đó.
        
    - `CTE 2`: Từ kết quả của CTE 1, tính tổng chi tiêu cho mỗi `customer_id`.
        
    - Truy vấn cuối cùng: Tìm khách hàng có tổng chi tiêu cao nhất từ CTE 2.
        

**6. (CTE để cải thiện logic) Tìm các sản phẩm được bán cùng với 'Laptop Dell XPS 15':**

- Viết một truy vấn để tìm tất cả các sản phẩm khác đã được mua trong cùng những đơn hàng có chứa 'Laptop Dell XPS 15'.
    
- _Gợi ý: Sử dụng một CTE để tìm tất cả các `order_id` có chứa 'Laptop Dell XPS 15'. Sau đó, `JOIN` CTE này với `Order_Items` để tìm các sản phẩm khác trong cùng các đơn hàng đó._
    

#### **Phần 3: Mệnh đề điều kiện (CASE WHEN)**

**7. (`CASE WHEN`) Phân loại sản phẩm theo mức giá:**

- Viết một truy vấn để hiển thị `product_name`, `unit_price` và một cột mới có tên `price_category`. Phân loại sản phẩm như sau:
    
    - 'Giá rẻ' nếu `unit_price` < $50.
        
    - 'Tầm trung' nếu `unit_price` từ $50 đến $200.
        
    - 'Cao cấp' nếu `unit_price` > $200.
        

**8. (`CASE WHEN` với hàm tổng hợp) Đếm số lượng đơn hàng theo trạng thái giao hàng:**

- Viết một truy vấn duy nhất để đếm tổng số đơn hàng đã được giao (`shipped_date` không phải `NULL`) và tổng số đơn hàng chưa được giao (`shipped_date` là `NULL`). Kết quả phải có 2 cột: `shipped_orders_count` và `unshipped_orders_count`.
    

#### **Phần 4: Bài tập kết hợp**

**9. (Kết hợp CTE và `CASE WHEN`) Xếp hạng khách hàng:**

- Sử dụng CTE để tính tổng chi tiêu của mỗi khách hàng. Sau đó, trong truy vấn cuối cùng, hãy sử dụng `CASE WHEN` để xếp hạng khách hàng thành các nhóm:
    
    - 'VIP' nếu tổng chi tiêu > $2000.
        
    - 'Thân thiết' nếu tổng chi tiêu từ $500 đến $2000.
        
    - 'Tiềm năng' nếu tổng chi tiêu < $500.
        
- Báo cáo cần hiển thị `customer_id`, họ tên đầy đủ, tổng chi tiêu, và hạng khách hàng (`customer_rank`).
    

**10. (Kết hợp Subquery, CTE, và `CASE WHEN`) Báo cáo hiệu suất nhân viên:**

- Viết một truy vấn phức tạp để tạo báo cáo hiệu suất nhân viên trong tháng 6 và tháng 7 năm 2025.
    
- **Yêu cầu:**
    
    1. Sử dụng một **CTE** để tính tổng doanh thu và số lượng đơn hàng mà mỗi nhân viên đã xử lý.
        
    2. Trong truy vấn cuối cùng, `JOIN` kết quả CTE với bảng `Employees`.
        
    3. Sử dụng một **Subquery** để tìm ra doanh thu trung bình trên mỗi nhân viên.
        
    4. Sử dụng `CASE WHEN` để tạo cột `performance_rating` dựa trên tổng doanh thu của nhân viên so với doanh thu trung bình:
        
        - 'Vượt trội' nếu doanh thu của họ lớn hơn 150% doanh thu trung bình.
            
        - 'Đạt yêu cầu' nếu doanh thu của họ từ 80% đến 150% doanh thu trung bình.
            
        - 'Cần cải thiện' nếu doanh thu của họ thấp hơn 80% doanh thu trung bình.
            
- Báo cáo cuối cùng cần có: `employee_id`, họ tên nhân viên, tổng số đơn hàng, tổng doanh thu, và `performance_rating`.
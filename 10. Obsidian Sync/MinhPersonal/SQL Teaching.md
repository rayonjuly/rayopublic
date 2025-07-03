### Giáo trình SQL: Các khái niệm Cốt lõi và Phép kết hợp (JOIN)

Nội dung này được thiết kế để dạy cho học viên mới bắt đầu về các khái niệm nền tảng của cơ sở dữ liệu quan hệ và cách kết hợp dữ liệu từ nhiều bảng bằng `JOIN`. Chúng ta sẽ sử dụng cơ sở dữ liệu `store_db` để làm ví dụ thực tế.

### **Phần 1: Khái niệm Cốt lõi của Cơ sở dữ liệu**

Mục tiêu của phần này là giúp học viên hiểu được cách dữ liệu được tổ chức và lưu trữ một cách có cấu trúc.

#### **1. Dataset (Tập dữ liệu) là gì?**

- **Khái niệm:** Một "Dataset" chỉ đơn giản là một tập hợp dữ liệu. Nó có thể là bất cứ thứ gì, từ một danh sách tên trong file Excel, một bộ sưu tập hình ảnh, cho đến một hệ thống phức tạp như cơ sở dữ liệu của một trang web thương mại điện tử.
    
- **Trong SQL:** Cơ sở dữ liệu (database) mà chúng ta đang làm việc (`store_db`) chính là một dataset. Điểm khác biệt là nó được tổ chức một cách rất logic và có cấu trúc để chúng ta có thể truy vấn và quản lý dữ liệu một cách hiệu quả.
    

#### **2. Table (Bảng)**

- **Khái niệm:** Một bảng là thành phần cơ bản nhất của một cơ sở dữ liệu. Hãy tưởng tượng nó như một trang tính (spreadsheet) trong Excel. Mỗi bảng chứa dữ liệu về một chủ đề cụ thể.
    
    - **Cột (Column/Field):** Đại diện cho một thuộc tính hoặc một loại thông tin. Ví dụ, trong bảng `Customers`, chúng ta có các cột như `first_name`, `last_name`, `email`.
        
    - **Hàng (Row/Record):** Đại diện cho một thực thể hoặc một bản ghi cụ thể. Mỗi hàng trong bảng `Customers` là thông tin về một khách hàng riêng biệt.
        
- **Ví dụ thực tế (Bảng `Customers`):**
    
    ```
    +-------------+------------+-----------+---------------------------+
    | customer_id | first_name | last_name | email                     |
    +-------------+------------+-----------+---------------------------+
    | 1           | Minh       | Nguyen    | minh.nguyen@example.com   |  <-- Một hàng (record)
    | 2           | Linh       | Tran      | linh.tran@example.com     |
    +-------------+------------+-----------+---------------------------+
                      ^
                      |---- Một cột (column)
    ```
    

#### **3. Primary Key (PK - Khóa chính)**

- **Mục đích:** Khóa chính là "chứng minh nhân dân" của mỗi hàng trong một bảng. Nó dùng để **định danh duy nhất** cho mỗi bản ghi.
    
- **Đặc điểm quan trọng:**
    
    1. **Không được chứa giá trị `NULL` (NOT NULL):** Mọi hàng bắt buộc phải có giá trị cho khóa chính.
        
    2. **Phải là duy nhất (UNIQUE):** Không có hai hàng nào trong cùng một bảng có thể có cùng một giá trị khóa chính.
        
- **Ví dụ thực tế:**
    
    - Trong bảng `Customers`, cột `customer_id` là khóa chính. Chúng ta có thể có nhiều người tên "Minh Nguyen", nhưng mỗi người sẽ có một `customer_id` hoàn toàn khác nhau.
        
    - Trong bảng `Products`, `product_id` là khóa chính.
        

#### **4. Foreign Key (FK - Khóa ngoại)**

- **Mục đích:** Khóa ngoại là "sợi dây liên kết" giữa các bảng. Nó tạo ra một mối quan hệ giữa hai bảng.
    
- **Khái niệm:** Một khóa ngoại trong một bảng là một cột (hoặc tập hợp các cột) tham chiếu đến khóa chính của một bảng khác.
    
- **Ví dụ thực tế (Liên kết `Customers` và `Orders`):**
    
    - Bảng `Customers` có khóa chính là `customer_id`.
        
    - Bảng `Orders` cũng có một cột tên là `customer_id`.
        
    - Cột `customer_id` trong bảng `Orders` chính là **khóa ngoại**. Nó cho chúng ta biết đơn hàng đó thuộc về khách hàng nào. Giá trị trong cột `Orders.customer_id` phải tương ứng với một giá trị `customer_id` đã tồn tại trong bảng `Customers`.
        
    
    ```
    Bảng Customers:                  Bảng Orders:
    +-------------+-------+          +----------+-------------+------------+
    | customer_id | name  |          | order_id | customer_id | order_date |
    +-------------+-------+          +----------+-------------+------------+
    | 1           | Minh  | <----    | 1        | 1           | 2025-06-10 |
    | 2           | Linh  |   |      | 2        | 2           | 2025-06-11 |
    +-------------+-------+   |----->| 3        | 1           | 2025-06-12 |
                              ^      +----------+-------------+------------+
                              |
                        Liên kết được tạo bởi Foreign Key
    ```
    
- **Tại sao lại cần khóa?** Việc chia dữ liệu ra nhiều bảng và liên kết chúng bằng khóa giúp:
    
    - **Giảm sự trùng lặp:** Chúng ta không cần lặp lại tên, email của khách hàng trong mỗi đơn hàng họ đặt.
        
    - **Đảm bảo tính nhất quán:** Dữ liệu khách hàng chỉ cần cập nhật ở một nơi duy nhất (bảng `Customers`).
        

### **Phần 2: Kết hợp Dữ liệu với `JOIN`**

Mục tiêu của phần này là dạy học viên cách lấy dữ liệu từ nhiều bảng cùng một lúc.

#### **1. Tại sao chúng ta cần `JOIN`?**

Như đã thấy ở trên, dữ liệu được chia nhỏ ra nhiều bảng. Nếu chúng ta muốn trả lời một câu hỏi như: "Khách hàng Minh Nguyen đã đặt những đơn hàng nào?", chúng ta không thể chỉ xem một bảng. Chúng ta cần lấy thông tin từ bảng `Customers` (để tìm `customer_id` của "Minh Nguyen") và sau đó dùng ID đó để tìm các đơn hàng trong bảng `Orders`.

`JOIN` là câu lệnh cho phép chúng ta **kết hợp các hàng từ hai hoặc nhiều bảng** dựa trên một cột liên quan giữa chúng (thường là khóa ngoại và khóa chính).

#### **2. `INNER JOIN` 

- **Khái niệm:** `INNER JOIN` trả về các bản ghi có giá trị khớp ở cả hai bảng. Nó giống như tìm phần giao nhau giữa hai tập hợp.
    
- **Sơ đồ Venn:**
    
- **Ví dụ thực tế:** "Lấy danh sách các đơn hàng và tên của khách hàng tương ứng."
    
    - Chúng ta chỉ muốn những đơn hàng có thông tin khách hàng rõ ràng, và chỉ những khách hàng đã từng đặt hàng.
        
    
    ```
    SELECT
        o.order_id,
        o.order_date,
        c.first_name,
        c.last_name
    FROM Orders AS o
    INNER JOIN Customers AS c ON o.customer_id = c.customer_id;
    ```
    
    - `ON o.customer_id = c.customer_id` là điều kiện kết hợp. Nó nói với SQL: "Hãy nối một hàng từ bảng `Orders` với một hàng từ bảng `Customers` nếu giá trị `customer_id` của chúng giống nhau."
        

#### **3. `LEFT JOIN` 

- **Khái niệm:** `LEFT JOIN` trả về **tất cả các bản ghi từ bảng bên trái** (bảng đầu tiên được liệt kê) và các bản ghi khớp từ bảng bên phải. Nếu không có sự khớp nào, các cột của bảng bên phải sẽ có giá trị `NULL`.
    
- **Sơ đồ Venn:**
    
- **Ví dụ thực tế:** "Liệt kê TẤT CẢ khách hàng và cho biết họ đã đặt bao nhiêu đơn hàng."
    
    - Chúng ta muốn có danh sách của tất cả khách hàng, kể cả những người chưa bao giờ mua hàng.
        
    
    ```
    SELECT
        c.first_name,
        c.last_name,
        o.order_id
    FROM Customers AS c
    LEFT JOIN Orders AS o ON c.customer_id = o.customer_id;
    ```
    
    - Kết quả sẽ hiển thị tất cả khách hàng. Đối với những khách hàng chưa có đơn hàng nào, cột `order_id` sẽ là `NULL`. Đây là cách phổ biến để tìm các bản ghi không có sự tương ứng ở bảng khác.
        

#### **4. `RIGHT JOIN` 

- **Khái niệm:** `RIGHT JOIN` hoạt động ngược lại với `LEFT JOIN`. Nó trả về **tất cả các bản ghi từ bảng bên phải** và các bản ghi khớp từ bảng bên trái. Nếu không có sự khớp nào, các cột của bảng bên trái sẽ có giá trị `NULL`.
    
- **Sơ đồ Venn:**
    
- **Ví dụ thực tế:** "Liệt kê TẤT CẢ sản phẩm và xem chúng đã được đặt trong đơn hàng nào."
    
    - Mục tiêu là xem sản phẩm nào chưa bao giờ được bán.
        
    
    ```
    SELECT
        p.product_name,
        oi.order_id,
        oi.quantity
    FROM Order_Items AS oi
    RIGHT JOIN Products AS p ON oi.product_id = p.product_id;
    ```
    
    - Những sản phẩm chưa từng xuất hiện trong bảng `Order_Items` sẽ vẫn được liệt kê, nhưng các cột `order_id` và `quantity` sẽ là `NULL`.
        
    - **Lưu ý cho học viên:** Hầu hết các truy vấn `RIGHT JOIN` đều có thể được viết lại thành `LEFT JOIN` bằng cách đảo ngược thứ tự các bảng. `LEFT JOIN` được sử dụng phổ biến hơn.
        

#### **5. `FULL OUTER JOIN` 

- **Khái niệm:** `FULL OUTER JOIN` trả về tất cả các bản ghi khi có sự khớp ở một trong hai bảng (trái hoặc phải). Về cơ bản, nó là sự kết hợp của cả `LEFT JOIN` và `RIGHT JOIN`.
    
- **Sơ đồ Venn:**
    
- **Lưu ý quan trọng:** **MySQL không hỗ trợ cú pháp `FULL OUTER JOIN` trực tiếp!** Thay vào đó, chúng ta mô phỏng nó bằng cách sử dụng `UNION` để kết hợp kết quả của một `LEFT JOIN` và một `RIGHT JOIN`.
    
    ```
    -- Đây là cách mô phỏng FULL OUTER JOIN trong MySQL
    SELECT *
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    UNION
    SELECT *
    FROM Customers c
    RIGHT JOIN Orders o ON c.customer_id = o.customer_id;
    ```
    
    - Câu lệnh này sẽ lấy: (1) Tất cả khách hàng và đơn hàng của họ, cộng với (2) Tất cả đơn hàng và khách hàng của chúng (để bao gồm cả trường hợp hiếm gặp là có đơn hàng mà không có khách hàng).
        

#### **6. `JOIN` nhiều bảng**

- **Khái niệm:** Bạn hoàn toàn có thể kết hợp nhiều hơn hai bảng trong một truy vấn duy nhất bằng cách nối chuỗi các lệnh `JOIN`.
    
- **Ví dụ thực tế:** "Hiển thị chi tiết đầy đủ của đơn hàng số 4: tên khách hàng, tên nhân viên xử lý, tên sản phẩm, số lượng, và tên nhà vận chuyển."
    
    - Để trả lời câu hỏi này, chúng ta cần dữ liệu từ 5 bảng khác nhau: `Orders`, `Customers`, `Employees`, `Order_Items`, `Products`, và `Shippers`.
        
    
    ```
    SELECT
        o.order_id,
        c.first_name AS customer_first_name,
        c.last_name AS customer_last_name,
        p.product_name,
        oi.quantity,
        e.first_name AS employee_first_name,
        s.shipper_name
    FROM Orders AS o
    INNER JOIN Customers AS c ON o.customer_id = c.customer_id
    INNER JOIN Employees AS e ON o.employee_id = e.employee_id
    INNER JOIN Order_Items AS oi ON o.order_id = oi.order_id
    INNER JOIN Products AS p ON oi.product_id = p.product_id
    LEFT JOIN Shippers AS s ON o.shipper_id = s.shipper_id -- LEFT JOIN vì có thể có đơn hàng chưa được giao
    WHERE o.order_id = 4;
    ```
    
    - Truy vấn này cho thấy sức mạnh của `JOIN` trong việc tổng hợp thông tin từ khắp nơi trong cơ sở dữ liệu để tạo ra một báo cáo có ý nghĩa.
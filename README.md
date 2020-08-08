# NguyenDucCong_18020245_Nhom1_Crawler
# Mã nguồn : Python + Scrapy

name :tên của spider và các spider không được đặt các name giống nhau.<br/>
allowed_domains:vùng cho phép crawl dữ liệu.<br/>
start_urls:<br/>
Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:<br/>
Kiểm tra xem link đó có phải là link cần crawl không (tránh crawl các link rác)<br/>
Sau khi kiểm tra thì ghi lại :link, title, description, content, category, time, keywords, author ra file.txt.<br/>
yield from : cho phép chỉ tiến hành crawl trên các bài báo có dạng "https://www.24h.com.vn" và callback lại parse.<br/>

# Các công việc đã thực hiện được: lấy được link, title, description, content, category, time, keywords, author của một bài viết.
# Kết quả : đã thu nhập được ~200 bài viết trừ trang https://www.24h.com.vn và các bài viết được đặt trong file 24h.txt và 24hV2 nằm trong mục Output, ngoài ra còn thu thập từ baomoi.com.

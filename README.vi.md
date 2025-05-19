# :rocket: Prompt Enhancer
#### Kỹ Thuật Prompt Engineering Ngay Trong Tầm Tay!

Chào mừng đến với bộ công cụ Prompt Enhancer, một ứng dụng được xây dựng bằng Streamlit để cải thiện prompt của bạn một cách dễ dàng. Công cụ này tích hợp nhiều nguyên tắc kỹ thuật prompt engineering, được nêu trong bài giảng [Prompting and Complex Reasoning](https://phontron.com/class/anlp-fall2024/assets/slides/anlp-07-prompting.pdf). Với Prompt Enhancer, bạn có thể dễ dàng áp dụng các kỹ thuật prompt engineering đã được nghiên cứu mới nhất xác nhận thông qua giao diện thân thiện với người dùng, nâng cao khả năng giao tiếp với các mô hình AI.


## Bắt Đầu Sử Dụng

### 1. Môi trường:

   Python 3 v3.10 (recommend) - Higher version may be not compatibility!

### 2. Cài đặt cục bộ:
1. **Sao chép repository Prompt Enhancer**:
   ```
   git clone https://github.com/caprocute/Promting-and-complexing-reasoning.git
   ```
2. **Cài đặt các gói cần thiết**:
   ```
   pip install -r requirements.txt
   ```
3. **Lấy API key OpenAI**:
   Bạn có thể lấy API key OpenAI của mình [tại đây](https://platform.openai.com/api-keys)
4. **Chạy Prompt Enhancer**:
   ```
   streamlit run main.py
   ```


## Cách Sử Dụng

1. **Nhập Prompt**: Nhập prompt bạn muốn cải thiện vào khu vực văn bản được chỉ định.
2. **Áp Dụng Kỹ Năng**: Chọn các kỹ năng bạn muốn áp dụng để tinh chỉnh prompt của mình.
3. **Thêm Cụm Từ**: Chọn xem có muốn thêm các cụm từ cụ thể để hướng dẫn AI tạo ra câu trả lời tốt hơn không.
4. **Cải Thiện**: Nhấp vào nút "Enhance!" để áp dụng các lựa chọn của bạn và xem prompt đã được cải thiện.


## Nghiên Cứu và Nguồn Cảm Hứng

Prompt Enhancer tích hợp nhiều kỹ thuật prompt engineering dựa trên các nguyên tắc từ bài báo của VILA-Lab [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4 (2024)](https://arxiv.org/pdf/2312.16171.pdf).
Ngoài ra, công cụ này còn cho phép người dùng tích hợp các prompt cảm xúc như "Điều này rất quan trọng đối với sự nghiệp của tôi", được lấy cảm hứng từ nghiên cứu của Microsoft [Large Language Models Understand and Can Be Enhanced by Emotional Stimuli (2023)](https://arxiv.org/pdf/2307.11760.pdf). Người dùng cũng có thể chọn thêm các cụm từ như "Hãy hít thở sâu và giải quyết vấn đề này từng bước một", khuyến khích AI đưa ra câu trả lời tốt hơn, được xác nhận bởi nghiên cứu của Google DeepMind [Large Language Models as Optimizers (2023)](https://arxiv.org/pdf/2309.03409.pdf).


## Công Nghệ Sử Dụng

1. **Streamlit**: Tạo giao diện người dùng trực quan cho trải nghiệm người dùng hấp dẫn.
2. **LangChain**: Tích hợp liền mạch các mô hình ngôn ngữ lớn vào ứng dụng.
3. **OpenAI API**: Kết nối với các mô hình của OpenAI để cung cấp khả năng cải thiện prompt theo thời gian thực.


## Liên Hệ Phản Hồi

- **Email**: lim.gadi@gmail.com
- **GitHub**: [@lim-hyo-jeong](https://github.com/lim-hyo-jeong)
- **Linkedin**: https://www.linkedin.com/in/lim-hyo-jeong/ 

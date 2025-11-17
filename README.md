# Balanced Binary Tree

## تعريف

شجرة ثنائية (Binary Tree) تكون **متوازنة** إذا **الفرق بين عمق الفرعين الأيمن والأيسر لأي عقدة لا يزيد عن 1**.

---

## مثال

### شجرة متوازنة

   3
 /   \
9     20
     /  \
    15   7

- الفرق بين العمق الأيسر والأيمن لكل عقدة ≤ 1  
- النتيجة: True

### شجرة غير متوازنة

   1
  / \
 2   2
/ \

- بعض العقد الفرق > 1  
- النتيجة: False

---

## طريقة الحل

1. نستخدم **Recursion** لحساب عمق كل عقدة.
2. لكل عقدة:
   - نحسب عمق الفرع الأيسر.
   - نحسب عمق الفرع الأيمن.
   - إذا الفرق > 1 → نعيد False.
3. إذا كل العقد الفرق ≤ 1 → نعيد True.

---

## الكود بلغة Python

```python
# شاهد ملف balanced_tree.py
python balanced_tree.py
# Output:
# Tree 1 is balanced: True
# Tree 2 is balanced: False

---

## 4️⃣ نشر المشروع على GitHub

1. إنشاء مستودع جديد على GitHub باسم `BalancedBinaryTree`.
2. في جهازك:

```bash
git init
git add .
git commit -m "Initial commit: Balanced Binary Tree in Python"
git branch -M main
git remote add origin <رابط المستودع الخاص بك>
git push -u origin main

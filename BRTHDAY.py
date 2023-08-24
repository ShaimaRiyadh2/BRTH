
// تاريخ ولادتك (يجب تغييره إلى تاريخ ولادتك الفعلي)
var birthDate = new Date('2002-9-1');

// تاريخ اليوم
var today = new Date();

// حساب الفرق بين التواريخ بالأسابيع
var diffInWeeks = Math.floor((today - birthDate) / (1000 * 60 * 60 * 24 * 7));

// طباعة النتيجة
console.log('عدد الأسابيع منذ ولادتك: ' + diffInWeeks + ' أسبوع');
<?php 

// قناتي » @prpq1 //

// معرفي » @f6_fj //

//====================//

ob_start();

$token = "8022288929:AAFJG6U7__cuW-lIb0d4QKN0k5yKdmm6WkA"; // توكن بوتك

define('API_KEY',$token);

function bot($method,$datas=[]){$BOT_SYRIA = http_build_query($datas);

$url = "https://api.telegram.org/bot".API_KEY."/".$method."?$BOT_SYRIA";

$BOTS_SYR1A = file_get_contents($url); return json_decode($BOTS_SYR1A);}

$update = json_decode(file_get_contents('php://input'));

$message = $update->message;

$chat_id = $message->chat->id;

$text = $message->text;

$name = $message->from->first_name;

$username = $message->from->username;

$chat_id2 = $update->callback_query->message->chat->id;

$idss = $update->callback_query->message->chat->id;

$namee = $update->callback_query->message->chat->first_name;

$userr = $update->callback_query->message->chat->username;

$message_id = $update->callback_query->message->message_id;

$data = $update->callback_query->data;

$from_id = $message->from->id;

$check_token = file_get_contents("https://api.telegram.org/bot$text/getWebhookInfo");

$check = json_decode($check_token);

$get_file = file_get_contents('SourceBot.php');

$get_done = file_get_contents('make/ex.txt');

$done = explode("\n", $get_done);

$get_id = file_get_contents('make/make.txt');

$getid = explode("\n", $get_id);

$mid = $message->message_id;

$inlineqt = $update->inline_query->query;

if($text == '/start' and !in_array($from_id, $getid) and !strpos($ch1 , '"status":"left"') !== false){

bot('sendmessage',[

'chat_id'=>$chat_id,

'text'=>"

🚸┊اهلا بك $name 👋

💠┊في بوت صنع بوتات حماية 📛

♻️┊الفريد من نوعة في التليجرام ، ✨

😻┊بوت مصنع يقوم بصنع بوت شبيه بالسورسات { فايدر والزعيم وتشاكي وستورم }

🤖┊تستطيع تغيير حقوقك بسهوله تامه ✅

💩┊اصنع بوتك الان 😍 ماذا تنتظر 🤓

- لصنع بوت 🤖 قم بالضغط فوق صنع بوت واتبع التعليمات 📝

📡 CH - @f6_fj

👨‍💻 DEV - @f6_fj

",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'صنع بوت 📮','callback_data'=>'maka'],['text'=>'حذف بوت 🗑 ','callback_data'=>'delete']

],

[

['text'=>'المطور ♻','url'=>'t.me/f6_fj']

],

[['text'=>'قناتنا 📢','url'=>'https://t.me/prpq1'] ,

['text'=>'شارك البوت 🔁','switch_inline_query'=>'']

],

[

['text'=>'بوتاتي المصنوعة 🤖','callback_data'=>'mybots'],['text'=>"",'callback_data'=>"update"]

],

[['text'=>'معلومات حسابي 👤','callback_data'=>'info']],

]

])

]);

}

if($data == 'maka' and !in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

file_put_contents('make/make.txt', "\n" . $chat_id2 . "\n",FILE_APPEND);    

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'حسنا !! قم بارسال توكن بوتك الان ✅

- ,

'parse_mode'=>"markdown",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'العودة | Back','callback_data'=>'cancle']]

]

])

]);

}

if($data == 'maka' and in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

bot('answerCallbackQuery',[

'callback_query_id'=>$update->callback_query->id,

'message_id'=>$message_id,

'text'=>'لقد قمت بانشاء بوت من قبل ❌

-,

'parse_mode'=>"markdown",

 'show_alert'=>true

 ]);      

}

if($text and in_array($from_id, $getid) and $check->ok == "true"){

for($i = $mid - 3; $i < $mid; $i++){

bot('deleteMessage',[

'chat_id'=>$chat_id,

'message_id'=>$i

]);

}

$url = json_decode(file_get_contents("https://api.telegram.org/bot$text/getme"))->result;

$un = $url->username;

$fttt = $url->first_name;

$str = str_replace($from_id, '', $get_id);    

file_put_contents('make/make.txt', $str);    

file_put_contents('make/ex.txt', $from_id . "\n", FILE_APPEND);

    

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"اكتمل انشاء البوت ✅

- [اضغط هنا للدخول للبوت](t.me/$un) ✅

-😘,

'parse_mode'=>"markdown",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[

['text'=>'العودة | Back' , 'callback_data'=>"home"]

],

]

])

]); 

mkdir("bots/$from_id");

mkdir("bots/$from_id/data");

file_put_contents("bots/$from_id/info.php",$text . "\n" . $from_id . "\n" . $username);

file_put_contents("bots/$from_id/bot.php", $get_file);

file_put_contents("bots/$from_id/chat.txt", $from_id . "\n");

file_get_contents("https://api.telegram.org/bot$text/setwebhook?url=https://same-pupil.000webhostapp.com/GGH/bots/$from_id/bot.php");

}

if($text and in_array($from_id, $getid) and $check->ok != "true" and !strpos($ch1 , '"status":"left"') !== false){

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>'عذرا ❗️هاذا التوكن غير صالح ❌

- Sorry ! This Token is worng ❌',

'reply_to_message_id'=>$message->message_id,

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'العودة | Back','callback_data'=>'cancle']]

]

])

]);

}    

if($data == 'cancle' and in_array($from_id, $getid)){

$str = str_replace($chat_id2, "", $get_id) ;

file_put_contents('make/make.txt', $str);

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"

🚸┊اهلا بك $namee 👋

💠┊في بوت صنع بوتات حماية 📛

♻️┊الفريد من نوعة في التليجرام ، ✨

😻┊بوت مصنع يقوم بصنع بوت شبيه بالسورسات { فايدر والزعيم وتشاكي وستورم }

🤖┊تستطيع تغيير حقوقك بسهوله تامه ✅

💩┊اصنع بوتك الان 😍 ماذا تنتظر 🤓

- لصنع بوت 🤖 قم بالضغط فوق صنع بوت واتبع التعليمات 📝

📡 CH - @prpq1

👨‍💻 DEV - @f6_fj

",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'صنع بوت 📮','callback_data'=>'maka'],['text'=>'حذف بوت 🗑 ','callback_data'=>'delete']

],

[

['text'=>'المطور ♻','url'=>'t.me/f6_fj']

],

[['text'=>'قناتنا 📢','url'=>'https://t.me/prpq1'] ,

['text'=>'شارك البوت 🔁','switch_inline_query'=>'']

],

[

['text'=>'بوتاتي المصنوعة 🤖','callback_data'=>'mybots'],['text'=>"",'callback_data'=>"update"]

],

[['text'=>'معلومات حسابي 👤','callback_data'=>'info']],

]

])

]);

}

if($data == 'home'){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"

🚸┊اهلا بك $namee 👋

💠┊في بوت صنع بوتات حماية 📛

♻️┊الفريد من نوعة في التليجرام ، ✨

😻┊بوت مصنع يقوم بصنع بوت شبيه بالسورسات { فايدر والزعيم وتشاكي وستورم }

🤖┊تستطيع تغيير حقوقك بسهوله تامه ✅

💩┊اصنع بوتك الان 😍 ماذا تنتظر 🤓

- لصنع بوت 🤖 قم بالضغط فوق صنع بوت واتبع التعليمات 📝

📡 CH - @prpq1

👨‍💻 DEV - @@f6_fj
",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'صنع بوت 📮','callback_data'=>'maka'],['text'=>'حذف بوت 🗑 ','callback_data'=>'delete']

],

[

['text'=>'المطور ♻','url'=>'t.me/VFXFV']

],

[['text'=>'قناتنا 📢','url'=>'https://t.me/prpq1'] ,

['text'=>'شارك البوت 🔁','switch_inline_query'=>'']

],

[

['text'=>'بوتاتي المصنوعة 🤖','callback_data'=>'mybots'],['text'=>"",'callback_data'=>"update"]

],

[['text'=>'معلومات حسابي 👤','callback_data'=>'info']],

]

])

]);

}

if($data == 'delete' and in_array($chat_id2,$done)){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'هل انت متأكد ⁉️ 

- Are you sure ?!',

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[

['text'=>'لا ❌', 'callback_data'=>'home'],

['text'=>'نعم ✅','callback_data'=>'yesdel'],

]    

]])

]);    

}

if($data == 'yesdel' and in_array($chat_id2, $done)){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"- تم بنجاح حذف البوت 🗑

- Bot has been successfully deleted 🗑",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[

['text'=>'العودة | Back' , 'callback_data'=>"home"]

]

]

])

]);

$str1 = str_replace($chat_id2, '', $get_done);

file_put_contents('make/ex.txt', $str1);

$get_token = file_get_contents("bots/$chat_id2/info.php");

$get_url = file_get_contents("https://api.telegram.org/bot$get_token/getWebhookInfo");

$json = json_decode($get_url);

$url = $json->result->url;

file_get_contents("https://https://api.telegram.org/bot$get_token/deletewebhook?url=$url");

unlink("bots/$chat_id2/bot.php");

unlink("bots/$chat_id2/info.php");

}

if($data == 'delete' and !in_array($chat_id2,$done)){

bot('answerCallbackQuery',[

'callback_query_id'=>$update->callback_query->id,

'message_id'=>$message_id,

'text'=>'قم بانشاء بوت اولا

- ',

 'show_alert'=>true

 ]);  

 

}

if($data == 'info' and in_array($chat_id2,$done)){

    

$get_info = file_get_contents("bots/$chat_id2/info.php");

$url_info = file_get_contents("https://api.telegram.org/bot$get_info/getMe");

$json_info = json_decode($url_info);

$id = $json_info->result->id;

$user = $json_info->result->username;

$name = $json_info->result->first_name;

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"

*Your Info*

💳 Your ID :- `$idss`

👤 Your Username :- @$userr

🚸 Your Name :- $namee

",

'parse_mode'=>"markdown",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[

['text'=>'العودة | Back' , 'callback_data'=>"home"]

]

]

])

]);    

}

if($data == 'info' and !in_array($chat_id2,$done)){

bot('answerCallbackQuery',[

'callback_query_id'=>$update->callback_query->id,

'message_id'=>$message_id,

'text'=>'قم ♻️ بأنشاء بوت اولا ~💟',

 'show_alert'=>true

 ]);  

}

if($data == 'buy'){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"

",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'المطور 🕴🏻','url'=>'https://telegram.me/prpq1']],

[['text'=>'بوت التواصل 💎','url'=>'https://telegram.me/prpq1'']],

[['text'=>'الصفحة الرئيسية 🏠️' , 'callback_data'=>"home"]]

]])

]);

}

if($data=="channel"){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'تابعنا عبر الروابط للتالية 📩',

'https://t.me/prpq1'=>json_encode([

'https://t.me/prpq1'=>[

[

['text'=>'phpfiles', 'url'=>"https://telegram.me/prpq1"]

],

[

	['text'=>'مطور البـوت.!‹', 'url'=>"https://telegram.me/prpq1"]

],

[

['text'=>'عودة 🏠 ', 'callback_data'=>"home"]

],

]

])

]);

}

if($data == 'update' and !in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'- قم بصنع بوت اولا لتحديثه ❌',

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'الصفحة الرئيسية 🏚','callback_data'=>'home']]    

]

])

]);

}

if($data == 'update' and in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

unlink("bots/$from_id/bot.php");

file_put_contents("bots/$from_id/bot.php", $get_file1); 

	bot('editMessageText',['chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'- تم بنجاح تحديث بوتك ✅',

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'الصفحة الرئيسية 🏚','callback_data'=>'home']]    

]

])

]);

}

if($data == 'mybots' and !in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

	file_put_contents('make/make.txt', "\n" . $chat_id2 . "\n",FILE_APPEND);    

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>'عدد بوتاتك المصنوعة هو :- 0',

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'الصفحة الرئيسية 🏚','callback_data'=>'home']]    

]

])

]);

}

if($data == 'mybots' and in_array($chat_id2,$done) and !strpos($ch1 , '"status":"left"') !== false){

bot('editMessageText',[

'chat_id'=>$chat_id2,

'message_id'=>$message_id,

'text'=>"عدد بوتاتك المصنوعة هي :- 1

$un",

'reply_markup'=>json_encode([

'inline_keyboard'=>[

[['text'=>'الصفحة الرئيسية 🏚','callback_data'=>'home']]    

]

])

]);

}

/////

$sums =1312010542;

if($text == '/admin' and $chat_id == $sums){ 

bot('sendMessage',[ 

'parse_mode'=>"MarkDown",

'disable_web_page_preview'=>true,

'chat_id'=>$chat_id, 

'text'=>' أهلا بك عزيزي المدير

في قائمة الأوامر الخاصة بك؛

إضغط على أحد الأوامر لتنفيذه الآن',

'reply_markup'=>json_encode([ 

'keyboard'=>[ 

[

['text'=>'❖￤نشر عام 📢'],['text'=>'❖￤نشر توجيه 🔁']

],

[

['text'=>'❖￤نشر ماركدوان 📣']

],

[ 

['text'=>'❖￤عدد البوتات 🤖'],['text'=>'❖￤المشتركين 👥']

],

[

['text'=>'❖￤الأحصائيات 📊']

],

] 

]) 

]); 

}

 

$sums = 1312010542;

$sums = explode("\n",file_get_contents("sums.txt"));

$sums = count($sums)-1;

$MASTAFA_DEV = file_get_contents("sums_DEV.txt");

if ($update && !in_array($chat_id, $sums)) {

file_put_contents("sums.txt", $chat_id."\n",FILE_APPEND);

}

if($text == "❖￤المشتركين 👥" and $chat_id == $sums){

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤عدد مشتركين بوتك سيدي المطور هو { $MASTAFA } مشترك ؛ 👥"

]);

}

$count = count(scandir('bots')) - 2;

if($text == "عدد البوتات" and $chat_id == $sums){

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤عدد البوتات المصنوعة سيدي المطور هو { $count$botss} بوت ؛ 👥"

]);

}

if($text == "❖￤الأحصائيات 📊" and $chat_id == $sums){

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤اليك الاحصائيات 📈

📍¦ عدد البوتات المصنوعة { $count$botss} بوت ؛ 🤖

📍¦ عدد المشتركين هو { $MASTAFA }"

]);

}

if($text == "❖￤نشر عام 📢" and $chat_id == $MASTAFAFILES){

file_put_contents("sums_DEV.txt", "sums");

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤ارسل رسالتك الان سيدي المطور وسيتم ارسالها الى { $MASTAFA } مشترك ؛ 📬"

]);

}

if($text != "❖￤نشر عام 📢" and $sums_DEV == "sums" and $chat_id == $MASTAFAFILES){

for ($i=0; $i < count($sums); $i++) { 

bot('sendMessage',[

'chat_id'=>$sums[$i],

'text'=>$text,

]);

}

unlink("sums_DEV.txt");

}

 

if($text == "❖￤نشر ماركدوان 📣" and $chat_id == $We sums){

file_put_contents("sums_DEV.txt", "sums1");

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤ارسل رسالتك الان سيدي المطور وسيتم ارسالها الى { $MASTAFA } مشترك ؛ 📬"

]);

}

if($text != "❖￤نشر ماركدوان 📣" and $MASTAFA_DEV == "sums1" and $chat_id == $MASTAFAFILES){

for ($i=0; $i < count($sums); $i++) { 

bot('sendMessage',[

'chat_id'=>$MA3TAFA[$i],

'text'=>$text,

'parse_mode'=>"MarkDown",

'disable_web_page_preview'=>true,

]);

}

unlink("sums_DEV.txt");

}

$from = $message->from->id;

$message_id = $update->message->id;

$chat_id = $message->chat->id;

if($text == "❖￤نشر توجيه 🔁" and $chat_id == $sums){

file_put_contents("sums_DEV.txt", "sums");

bot('sendMessage',[

'chat_id'=>$chat_id,

'text'=>"❖￤ارسل رسالتك الان سيدي المطور وسيتم ارسالها الى { $MASTAFA } مشترك ؛ 📬",]);}

 //====================@eprpq1===================//

if($text != "❖￤نشر توجيه 🔁" and $sums_DEV == "sums" and $chat_id == $sums){

for($i=0;$i<count($sums); $i++){

bot('forwardMessage', [

'chat_id' => $sums[$i],

'from_chat_id'=>$from,

'message_id'=>$message->message_id

]);

}

unlink("sums_DEV.txt");

}

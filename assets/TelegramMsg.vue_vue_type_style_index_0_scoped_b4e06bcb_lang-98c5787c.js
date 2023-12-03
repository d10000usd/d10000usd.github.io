import{a,t as o}from"./telegramini-40e3a79c.js";import{r as n}from"./index-5d9bcfa2.js";const r="6"+o.t,g="1"+o.i,i=n(""),c=async e=>{try{const s=`

<span class="tg-spoiler">spoiler</span>
<b>Alarm</b> - <strong>Setting values enough</strong>
<i>Value changes </i> 
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji> 
<a href="http://112.165.191.22:8088/TsWebsocket_Report?message=%22KRW-BTC%22">Chart</a>



<strong>Suggest coin</strong>
<pre><code class="language-json">
${JSON.stringify(e.text.assets.Suggestcoin,null,2)}
</code></pre>

<strong>Upbit Amount</strong>
<pre><code class="language-json">
${JSON.stringify(e.text.assets.Amount,null,2)}
</code></pre>

<strong>Upbit UpbitAll</strong>
<pre><code class="language-json">
${JSON.stringify(e.text.assets.UpbitAll,null,2)}
</code></pre>
`;return(await a.post(`https://api.telegram.org/bot${r}/sendMessage`,{chat_id:g,text:s,parse_mode:"HTML"},{headers:{"Content-Type":"application/json"}})).data}catch(s){console.error("Error sending message:",s)}},u=async e=>{const s={text:e},t=await c(s);i.value=t?"ok":JSON.stringify(s)};export{i as m,u as s};

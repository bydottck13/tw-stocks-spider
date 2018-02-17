#!/usr/bin/env python
# -*- coding: utf-8 -*-
stock_ex_list = {'2301':'光寶科', '2302':'麗正', '2303':'聯電', '2305':'全友', '2308':'台達電子',
'2310':'旭麗', '2311':'日月光', '2312':'金寶', '2313':'華通', '2314':'台揚',
'2315':'神達', '2316':'楠梓電子', '2317':'鴻海', '2318':'佳錄', '2319':'大眾',
'2321':'東訊', '2322':'致福', '2323':'中環', '2324':'仁寶', '2325':'矽品',
'2327':'國巨', '2328':'廣宇', '2329':'華泰', '2330':'台積電',
'2331':'精英', '2332':'友訊', '2333':'碧悠', '2335':'清三', '2336':'致伸',
'2337':'旺宏', '2338':'光罩', '2339':'合泰', '2340':'光磊', '2341':'英群',
'2342':'茂矽', '2343':'精業', '2344':'華邦電子', '2345':'智邦', '2347':'聯強',
'2348':'力捷', '2349':'錸德', '2350':'環電', '2351':'順德', '2352':'明基',
'2353':'宏碁', '2354':'華升', '2355':'敬鵬', '2356':'英業達 ', '2357':'華碩',
'2358':'美格', '2359':'所羅門', '2360':'致茂', '2361':'鴻友', '2362':'藍天',
'2363':'矽統', '2364':'倫飛', '2365':'昆盈', '2366':'亞旭', '2367':'燿華',
'2368':'金像電子', '2369':'菱生', '2370':'匯僑工業', '2371':'大同', '2373':'震旦行',
'2374':'佳能', '2375':'智寶', '2376':'技嘉', '2377':'微星', '2378':'鴻運電子',
'2379':'瑞昱', '2380':'虹光', '2381':'華宇', '2382':'廣達', '2383':'台光電子',
'2384':'勝華', '2385':'群光', '2386':'國電', '2387':'精元', '2388':'威盛',
'2389':'世昕', '2390':'云辰', '2391':'合勤', '2392':'正崴', '2393':'億光',
'2394':'普立爾', '2395':'研華', '2396':'精碟', '2397':'友通資訊', '2398':'博達',
'2399':'映泰', '2401':'凌陽', '2402':'毅嘉', '2403':'友尚', '2404':'漢唐',
'2405':'浩鑫', '2406':'國碩', '2407':'陞技', '2408':'南科', '2409':'友達',
'2410':'普大', '2411':'飛瑞', '2412':'中華電', '2413':'環科', '2414':'精技',
'2415':'錩新', '2416':'世平', '2417':'圓剛', '2418':'雅新', '2419':'仲琦',
'2420':'新巨', '2421':'建準', '2422':'國聯', '2423':'固緯', '2424':'隴華',
'2425':'承啟', '2426':'鼎元', '2427':'三商電 ', '2428':'興勤', '2429':'永兆',
'2430':'燦坤', '2431':'聯昌', '2432':'倚天', '2433':'互盛電', '2434':'統懋',
'2435':'台路', '2436':'偉詮電', '2437':'旺詮', '2438':'英誌', '2439':'美律',
'2440':'太空梭', '2441':'超豐', '2442':'美齊', '2443':'利碟', '2444':'友旺',
'2445':'南方', '2446':'全懋', '2447':'鼎新', '2448':'晶電', '2449':'京元電',
'2450':'神腦', '2451':'創見', '2452':'乾坤', '2453':'凌群', '2454':'聯發科',
'2455':'全新', '2456':'奇力新', '2457':'飛宏', '2458':'義隆', '2459':'敦吉',
'2460':'建通', '2461':'光群雷', '2462':'良得電', '2463':'研揚', '2464':'盟立',
'2465':'麗臺', '2466':'冠西電', '2467':'志聖', '2468':'華經', '2469':'力信',
'2470':'品佳', '2471':'資通', '2472':'立隆電', '2473':'思源', '2474':'可成',
'2475':'華映', '2476':'鉅祥', '2477':'美隆電', '2478':'大毅', '2479':'和立',
'2480':'敦陽科', '2481':'強茂', '2482':'連宇', '2483':'百容', '2484':'希華',
'2485':'兆赫', '2486':'一詮', '2487':'友立資', '2488':'漢平', '2489':'瑞軒',
'2490':'皇統', '2491':'訊碟', '2492':'華新科', '2493':'揚博', '2494':'突破',
'2495':'普安', '2496':'卓越', '2497':'怡利電', '2498':'宏達電 ', '2499':'東貝',
'3001':'協和', '3002':'歐格', '3003':'健和興', '3004':'宏達科 ', '3005':'神基',
'3006':'晶豪科', '3007':'綠點', '3008':'大立光電', '3009':'奇美電', '3010':'華立',
'3011':'今皓', '3012':'廣輝', '3013':'晟銘電', '3014':'聯陽', '3015':'全漢',
'3016':'嘉晶', '3017':'奇鋐', '3018':'同開', '3019':'亞光', '3020':'奇普仕',
'3021':'衛道', '3022':'威達電', '3023':'信邦', '3024':'憶聲', '3025':'星通',
'3026':'禾伸堂', '3027':'盛達', '3028':'增你強', '3029':'零壹', '3030':'德律',
'3031':'佰鴻', '3032':'偉訓', '3033':'威健', '3034':'聯詠', '3035':'智原',
'3036':'文曄', '3037':'欣興', '3038':'全台', '3039':'宏傳', '3040':'遠見',
'3041':'揚智', '3042':'晶技', '3043':'科風', '3044':'健鼎', '3045':'台灣大',
'3046':'建碁', '3047':'訊舟', '3048':'益登', '3049':'和鑫', '3050':'鈺德',
'3051':'力特', '3052':'夆典', '3053':'鼎營', '3054':'萬國', '3055':'蔚華科',
'3056':'駿億', '3057':'喬鼎', '3058':'立德', '3059':'華晶科 ', '3060':'銘異',
'3061':'璨圓', '6128':'上福'	}
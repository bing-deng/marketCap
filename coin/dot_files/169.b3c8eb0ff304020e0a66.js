(window.webpackJsonp_N_E=window.webpackJsonp_N_E||[]).push([[169],{"9GVF":function(e,t,n){"use strict";n.d(t,"b",(function(){return s})),n.d(t,"a",(function(){return f}));var r=n("q1tI"),i=n.n(r),o=n("0+Xt"),a=n("vOnD"),l=n("HvWY"),c=i.a.createElement,u=a.e.div.withConfig({componentId:"sc-9dqrx-0"})(["display:flex;flex-direction:row;align-items:center;justify-content:",";"],(function(e){return e.flexEnd?"flex-end":"flex-start"})),d=a.e.div.withConfig({componentId:"sc-9dqrx-1"})(["cursor:pointer;display:flex;flex-direction:row;align-items:center;span[class^='icon']{margin-left:1px;}"]),s=function(e){var t=e.text,n=e.sortKey,r=e.currentSortKey,i=e.sortDirection,a=e.onSort,s=e.align,f=e.textClassName,v=void 0===f?void 0:f,p=e.explainer,m=void 0===p?null:p,b=e.t,g=void 0===b?function(e){return e}:b;function h(){a(n,"asc"===i?"desc":"asc"),l.a.sendEvent({category:"Table Sort",action:n})}var w=m||null;return"left"===s?c(u,null,c(d,{onClick:h},c(o.a,{className:v,fontSize:0},t),r===n&&c("span","asc"===i?{className:"icon-Caret-up",style:{marginLeft:"4px"}}:{className:"icon-Caret-down",style:{marginLeft:"4px"}})),w&&c(w,{t:g})):c(u,{flexEnd:!0},c(d,{onClick:h},r===n&&c("span","asc"===i?{className:"icon-Caret-up",style:{marginRight:"4px"}}:{className:"icon-Caret-down",style:{marginRight:"4px"}}),c(o.a,{className:v,fontSize:0,style:{whiteSpace:"nowrap"}},t)),w&&c(w,{t:g}))},f=a.e.div.withConfig({componentId:"sc-9dqrx-2"})(["height:22px;font-size:11px;display:inline-flex;flex-direction:row;align-items:center;padding:0 4px;border-radius:4px;background-color:",";img{height:12px;width:12px;border-radius:6px;margin-right:4px;}"],(function(e){return e.theme.colors.neutral2}))},YAXG:function(e,t,n){"use strict";var r=n("wx14"),i=n("q1tI"),o=n.n(i),a=n("bx8S"),l=n("b3D7"),c=n("Ziws"),u=n("3Mlv"),d=n("9GVF"),s=o.a.createElement,f=o.a.memo((function(e){var t=e||{},n=t.data,a=void 0===n?[]:n,l=t.columns,c=void 0===l?[]:l,d=t.rowKey,f=t.insertRows,p=void 0===f?{}:f,b=t.fixedHeader,g=void 0===b||b,h=t.tableClassName,w=t.emptyText,x=void 0===w?"No Data":w,O=t.lazy,j=t.useInViewPort,y=t.loading,C=t.onRowClick,S=t.isShowTitle,D=void 0===S||S,I=t.tableHeaderRef,k=c.filter((function(e){return!!e})),N=a&&a.length,R=s("tbody",null,y?s("tr",null,s("td",{colSpan:k.length||5},s(u.a,{fullWidth:!0,style:{padding:"48px 0"}}))):N?a.map((function(e,t){return s(o.a.Fragment,{key:e[d]||t},p[t],s(m,{data:e,columns:k,rowIdx:t,lazy:O&&O(t),useInViewPort:j,onRowClick:C}))})):s("tr",null,s("td",{colSpan:k.length||5},x))),q=Object(i.useMemo)((function(){return k.some((function(e){return e.width}))&&0!==a.length?s("colgroup",null,k.map((function(e,t){var n,i,o={};e.width&&(o.style={width:null!==(n=e.width)&&void 0!==n?n:"auto",minWidth:null!==(i=e.minWidth)&&void 0!==i?i:"auto"});return s("col",Object(r.a)({},o,{key:t}))}))):null}),[k]);return s("table",{className:"cmc-table ".concat(h," ").concat(y?"cmc-table-loading":"")},q,N&&D?s(v,{columns:k,fixedHeader:g,tableHeaderRef:I}):null,R)})),v=o.a.memo((function(e){var t=e.columns,n=e.fixedHeader,r=e.tableHeaderRef;return s("thead",{ref:r},s("tr",null,t.map((function(e,t){return s("th",{key:t,className:n?"stickyTop":"",style:{textAlign:e.align,top:"number"===typeof n?n:void 0},onDrag:function(e){console.log(e)}},e.title)}))))})),p=["slug","star"],m=o.a.memo((function(e){var t=e.columns,n=e.data,r=e.rowIdx,o=e.lazy,c=e.useInViewPort,u=e.onRowClick,f=Object(i.useState)(!o),v=f[0],m=f[1];Object(i.useEffect)((function(){!o&&m(!0)}),[o]);var b=Object(i.useRef)(),g=Object(l.a)(b,c&&(!o||v));return v?s("tr",{ref:b,style:{cursor:u?"pointer":void 0},onClick:function(){return u&&u(n)}},t.map((function(e,t){return s("td",{key:t,style:{textAlign:e.align}},function(e){var t=e.c,n=e.data,r=e.rowIdx,i=e.inViewPort;if(0===(null===n||void 0===n?void 0:n.isActive)&&p.indexOf(null===t||void 0===t?void 0:t.dataIndex)<0)return s(d.a,null,"--");var o=void 0===n[t.dataIndex]?JSON.stringify(n):n[t.dataIndex];return t.render?t.render(o,n,r,i):o}({c:e,data:n,rowIdx:r,inViewPort:g}))}))):s(a.a,{PlaceHolder:o,trigger:function(){return m(!0)},rootMargin:"900px",data:n})}));t.a=Object(c.a)(f,(function(){return s("table",{className:"cmc-table"},s("tbody",null,s("tr",null,s("td",null,"Tabel Render Error!"))))}))},Ziws:function(e,t,n){"use strict";n.d(t,"a",(function(){return m}));var r=n("1OyB"),i=n("vuIU"),o=n("Ji7U"),a=n("md7G"),l=n("foSv"),c=n("q1tI"),u=n("vOnD"),d=n("X7K/"),s=c.createElement;function f(e){var t=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}();return function(){var n,r=Object(l.a)(e);if(t){var i=Object(l.a)(this).constructor;n=Reflect.construct(r,arguments,i)}else n=r.apply(this,arguments);return Object(a.a)(this,n)}}var v=function(e){Object(o.a)(n,e);var t=f(n);function n(e){var i;return Object(r.a)(this,n),(i=t.call(this,e)).state={error:!1},i}return Object(i.a)(n,[{key:"componentDidCatch",value:function(e){this.setState({error:!0})}},{key:"render",value:function(){var e=this.props.placeHolder;return this.state.error?s(e,null):this.props.children}}]),n}(c.PureComponent),p=u.e.div.withConfig({componentId:"gjwu8q-0"})(["font-size:16px;font-weight:500;text-align:center;color:var(--color-light-neutral-6);padding:16px 0;"]),m=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:function(){return s(p,null,"Oops! Something went wrong. ",s(d.a,{onClick:function(){return location.reload()}},"Try Again"))};return function(n){return s(v,{placeHolder:t},s(e,n))}}},bx8S:function(e,t,n){"use strict";n.d(t,"a",(function(){return u}));n("rePB");var r=n("wx14"),i=n("ODXe"),o=n("Ff2n"),a=n("q1tI"),l=n.n(a),c=l.a.createElement;var u=function(e){var t=e.rootMargin,n=void 0===t?"800px":t,u=e.threshold,d=void 0===u?.1:u,s=e.PlaceHolder,f=void 0===s?l.a.forwardRef((function(e,t){return c("div",{ref:t})})):s,v=e.trigger,p=void 0===v?function(){}:v,m=Object(o.a)(e,["rootMargin","threshold","PlaceHolder","trigger"]),b=Object(a.useRef)();return Object(a.useEffect)((function(){if(!window.IntersectionObserver)return p(!0);var e=new IntersectionObserver((function(t){var n=Object(i.a)(t,1)[0];n.isIntersecting&&(p(!0),e.unobserve(n.target),e=null)}),{rootMargin:n,threshold:d});e.observe(b.current)}),[]),c(f,Object(r.a)({ref:b},m))}},x1mG:function(e,t,n){"use strict";n.r(t);var r=n("ODXe"),i=n("BtMM"),o=n("u2zV"),a=n("p2Nt"),l=n("q1tI"),c=n.n(l),u=n("eSIs"),d=n("2ZDD"),s=n("YAXG"),f=n("WHii"),v=n("ttae"),p=n("ktqD"),m=n.n(p),b=n("uaRo"),g=n("X7K/"),h=n("Mv+J"),w=n("+Zue"),x=n("L2Vh"),O=n("oq0z"),j=n("qh75"),y=n("/MKj"),C=n("YG6n"),S=n("g7An"),D=c.a.createElement;t.default=function(){var e=Object(l.useContext)(a.CurrenciesPageContext),t=e.id,n=e.name,c=Object(l.useState)(Object(u.p)(Object(u.s)(2,void 0,!0),!0)),p=c[0],I=c[1],k=Object(l.useState)(Object(u.p)(new Date,!0)),N=k[0],R=k[1],q=Object(l.useState)([]),H=q[0],M=q[1],E=Object(l.useState)(!1),P=E[0],U=E[1],V=Object(y.e)(C.i),z=Object(j.a)(!0),_=Object(r.a)(z,2),A=_[0],T=_[1],Y=Object(f.c)().t,G=Object(l.useMemo)((function(){return[{title:Y("Date"),dataIndex:"time_open",align:"left",width:315,render:function(e){return Object(u.e)("MMM DD, YYYY",new Date(e),!0)}},{title:"".concat(Y("Open"),"*"),render:function(e,t){var n,r,i=null===t||void 0===t||null===(n=t.quote)||void 0===n||null===(r=n.USD)||void 0===r?void 0:r.open;return Object(v.c)(i)},width:120},{title:Y("High"),render:function(e,t){var n,r,i=null===t||void 0===t||null===(n=t.quote)||void 0===n||null===(r=n.USD)||void 0===r?void 0:r.high;return Object(v.c)(i)},width:120},{title:Y("Low"),render:function(e,t){var n,r,i=null===t||void 0===t||null===(n=t.quote)||void 0===n||null===(r=n.USD)||void 0===r?void 0:r.low;return Object(v.c)(i)},width:120},{title:"".concat(Y("Close"),"**"),render:function(e,t){var n,r,i=null===t||void 0===t||null===(n=t.quote)||void 0===n||null===(r=n.USD)||void 0===r?void 0:r.close;return Object(v.c)(i)},width:120},{title:Y("Volume"),render:function(e,t){var n,r,i=null===t||void 0===t||null===(n=t.quote)||void 0===n||null===(r=n.USD)||void 0===r?void 0:r.volume;return Object(v.c)(i,{decimal:0})},width:315},{title:Y("Market Cap"),render:function(e,t){var n=Object(S.Q)((function(){var e,n;return null===t||void 0===t||null===(e=t.quote)||void 0===e||null===(n=e.USD)||void 0===n?void 0:n.market_cap}),0);return Object(v.c)(n,{decimal:0})},align:"right",width:150}]}),[]);return Object(l.useEffect)((function(){T((function(){return Object(d.c)({id:[t],time_start:Object(u.o)(p),time_end:Object(u.o)(N)}).then((function(e){var t;M(((null===e||void 0===e||null===(t=e.data)||void 0===t?void 0:t.quotes)||[]).reverse())}))}))}),[p,N]),D("div",{className:m.a.wrapper},D(i.a,null,D(o.a,{mr:"24px",mb:"24px"},"Historical Data for ",n),D(b.a,{trigger:"mouseenter",arrow:!0,visible:P,maxWidth:1200,offset:[-120,10],onClickOutside:function(){return!Object(S.B)()&&U(!1)},interactive:!0,placement:"bottom",content:D(O.a,{date:[p,N],onSet:function(e,t){U(!1),I(e),R(t)},onCancel:function(){return U(!1)},range:!0,inline:!0})},D("span",{className:m.a.rangeBtn},D(g.a,{onClick:function(){return U(!0)},disabled:A,variant:"outline"},D(h.a,null),"Date Range\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0",D(P?w.a:x.a,null))))),D("div",{className:m.a.tableWrapper},D(s.a,{data:H,columns:G,rowKey:"time_open",tableClassName:m.a.table,fixedHeader:V?0:64,loading:A})),D("p",{style:{textAlign:"center"}},D(g.a,{onClick:function(){return I(new Date(Object(u.s)(1,p,!0)))},disabled:A},A?"Loading...":"Load More")),D("p",null,"* Earliest data in range (UTC time) ",D("br",null),"** Latest data in range (UTC time)"))}}}]);
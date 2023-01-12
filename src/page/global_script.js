const log = console.log,
	byId = document.getElementById.bind(document),
	byClass = document.getElementsByClassName.bind(document),
	byTag = document.getElementsByTagName.bind(document),
	byName = document.getElementsByName.bind(document),
	createElement = document.createElement.bind(document);


String.prototype.toHtmlEntities = function() {
	return this.replace(/./ugm, s => s.match(/[a-z0-9\s]+/i) ? s : "&#" + s.codePointAt(0) + ";");
};









function null_func() {
	return true
}

function line_break() {
	var br = createElement("br")
	return br
}

function toggle_scroll() {
	document.body.classList.toggle('overflowHidden');
}

function go_link(typee, locate) {
	// function to generate link for different types of actions
	return locate + "?" + typee;
}
// getting all the links in the directory

class Config {
	constructor() {
		this.total_popup = 0;
		this.popup_msg_open = false;
		this.allow_Debugging = true
		this.Debugging = false;
		this.Hammered_modal = 0;
		this.is_touch_device = 'ontouchstart' in document.documentElement;


		this.previous_type = null;
		this.themes = ["Tron"]



		this.is_webkit = navigator.userAgent.indexOf('AppleWebKit') != -1
		this.is_edge = navigator.userAgent.indexOf('Edg') != -1

	}
}
var config = new Config()


class Tools {
	// various tools for the page
	sleep(ms) {
		// sleeps for a given time in milliseconds
		return new Promise(resolve => setTimeout(resolve, ms));
	}
	onlyInt(str) {
		if (this.is_defined(str.replace)) {
			return parseInt(str.replace(/\D+/g, ""))
		}
		return 0;
	}
	del_child(elm) {
		if (typeof(elm) == "string") {
			elm = byId(elm)
		}
		while (elm.firstChild) {
			elm.removeChild(elm.lastChild);
		}
	}
	toggle_bool(bool) {
		return bool !== true;
	}
	exists(name) {
		return (typeof window[name] !== 'undefined')
	}
	hasClass(element, className, partial = false) {
		if (partial) {
			className = ' ' + className;
		} else {
			className = ' ' + className + ' ';
		}
		return (' ' + element.className + ' ').indexOf(className) > -1;
	}
	addClass(element, className) {
		if (!this.hasClass(element, className)) {
			element.classList.add(className);
		}
	}
	enable_debug() {
		if (!config.allow_Debugging) {
			alert("Debugging is not allowed");
			return;
		}
		if (config.Debugging) {
			return
		}
		config.Debugging = true;
		var script = createElement('script');
		script.src = "//cdn.jsdelivr.net/npm/eruda";
		document.body.appendChild(script);
		script.onload = function() {
			eruda.init()
		};
	}
	is_in(item, array) {
		return array.indexOf(item) > -1;
	}
	is_defined(obj) {
		return typeof(obj) !== "undefined"
	}
	toggle_scroll(allow = 2, by = "someone") {
		if (allow == 0) {
			document.body.classList.add('overflowHidden');
		} else if (allow == 1) {
			document.body.classList.remove('overflowHidden');
		} else {
			document.body.classList.toggle('overflowHidden');
		}
	}
	download(dataurl, filename = null) {
		const link = createElement("a");
		link.href = dataurl;
		link.download = filename;
		link.click();
	}

	full_path(rel_path){
		let fake_a = createElement("a")
		fake_a.href = rel_path;
		return fake_a.href;
	}


	async copy_2(ev, textToCopy) {
		// navigator clipboard api needs a secure context (https)
		if (navigator.clipboard && window.isSecureContext) {
			// navigator clipboard api method'
			await navigator.clipboard.writeText(textToCopy);
			return 1
		} else {
			// text area method
			let textArea = createElement("textarea");
			textArea.value = textToCopy;
			// make the textarea out of viewport
			textArea.style.position = "fixed";
			textArea.style.left = "-999999px";
			textArea.style.top = "-999999px";
			document.body.appendChild(textArea);
			textArea.focus();
			textArea.select();

			let ok=0;
				// here the magic happens
				if(document.execCommand('copy')) ok = 1

			textArea.remove();
			return ok

		}
	}

	fetch_json(url){
		return fetch(url).then(r => r.json()).catch(e => {console.log(e); return null;})
	}
}
let tools = new Tools();




'#########################################'
// tools.enable_debug() // TODO: Disable this in production
'#########################################'

class Popup_Msg {
	constructor() {
		this.create()
		this.made_popup = false;
		this.init()
	}
	init() {
		this.onclose = null_func;
		this.scroll_disabled = false;
	}
	create() {
		var that = this;
		let popup_id, popup_obj, popup_bg, close_btn, popup_box;

		popup_id = config.total_popup;



		popup_obj = createElement("div")
		popup_obj.id = "popup-" + popup_id;
		popup_obj.classList.add("popup")

		popup_bg = createElement("div")
		popup_bg.classList.add("modal_bg")
		popup_bg.id = "popup-bg-" + popup_id;
		popup_bg.style.backgroundColor = "#000000EE";
		popup_bg.onclick = function() {
			that.close()
		}

		popup_obj.appendChild(popup_bg);

		this.popup_obj = popup_obj
		this.popup_bg = popup_bg


		popup_box = createElement("div");
		popup_box.classList.add("popup-box")

		close_btn = createElement("div");
		close_btn.classList.add("popup-close-btn")
		close_btn.onclick = function() {
			that.close()
		}
		close_btn.innerHTML = "&times;";
		popup_box.appendChild(close_btn)
		this.header = createElement("h1")
		this.header.id = "popup-header-" + popup_id;
		popup_box.appendChild(this.header)
		this.hr = createElement("popup-hr-" + popup_id);
		this.hr.style.width = "95%"
		popup_box.appendChild(this.hr)
		this.content = createElement("div")
		this.content.id = "popup-content-" + popup_id;
		popup_box.appendChild(this.content)
		this.popup_obj.appendChild(popup_box)

		byId("popup-container").appendChild(this.popup_obj)
		config.total_popup += 1;
	}
	close() {
		this.onclose()
		this.dismiss()
		config.popup_msg_open = false;
		this.init()
	}
	hide() {
		this.popup_obj.classList.remove("active");
		tools.toggle_scroll(1)
	}
	dismiss() {
		this.hide()
		tools.del_child(this.header);
		tools.del_child(this.content);
		this.made_popup = false;
	}
	async togglePopup(toggle_scroll = true) {
		if (!this.made_popup) {
			return
		}
		this.popup_obj.classList.toggle("active");
		if (toggle_scroll) {
			tools.toggle_scroll();
		}
		// log(tools.hasClass(this.popup_obj, "active"))
		if (!tools.hasClass(this.popup_obj, "active")) {
			this.close()
		}
	}
	async open_popup(allow_scroll = false) {
		if (!this.made_popup) {
			return
		}
		this.popup_obj.classList.add("active");
		if (!allow_scroll) {
			tools.toggle_scroll(0);
			this.scroll_disabled = true;
		}
	}
	async createPopup(header = "", content = "", hr = true) {
		this.init()
		this.made_popup = true;
		if (typeof header === 'string' || header instanceof String) {
			this.header.innerHTML = header;
		} else if (header instanceof Element) {
			this.header.appendChild(header)
		}
		if (typeof content === 'string' || content instanceof String) {
			this.content.innerHTML = content;
		} else if (content instanceof Element) {
			this.content.appendChild(content)
		}
		if (hr) {
			this.hr.style.display = "block";
		} else {
			this.hr.style.display = "none";
		}

	}
}
let popup_msg = new Popup_Msg();

class Toaster {
	constructor() {
		this.container = createElement("div")
		this.container.classList.add("toast-box")
		this.toaster = createElement("div")
		this.toaster.classList.add("toast-body")

		this.container.appendChild(this.toaster)
		document.body.appendChild(this.container)

		this.BUSY = 0;
	}


	async toast(msg,time) {
		// toaster is not safe as popup by design
		var sleep = 3000;

		this.BUSY = 1;
		this.toaster.innerText = msg;
		this.container.classList.add("visible")
		if(tools.is_defined(time)) sleep = time;
		await tools.sleep(sleep)
		this.container.classList.remove("visible")
		this.BUSY = 0
	}
}

let toaster = new Toaster()



function r_u_sure({y=null_func, n=null, head="Head", body="Body", y_msg="Yes",n_msg ="No"}={}) {
	popup_msg.close()
	var box = createElement("div")
	var msggg = createElement("p")
	msggg.innerHTML = body; //"This can't be undone!!!"
	box.appendChild(msggg)
	var y_btn = createElement("div");
	y_btn.innerText = y_msg;//"Continue"
	y_btn.className = "pagination center";
	y_btn.onclick = y;/*function() {
		that.menu_click('del-p', file);
	};*/
	var n_btn = createElement("div");
	n_btn.innerText = n_msg;//"Cancel"
	n_btn.className = "pagination center";
	n_btn.onclick = () => {return (n==null) ? popup_msg.close() : n()};
	box.appendChild(y_btn);
	box.appendChild(line_break());
	box.appendChild(n_btn);
	popup_msg.createPopup(head, box) ; //"Are you sure?"
	popup_msg.open_popup();
}

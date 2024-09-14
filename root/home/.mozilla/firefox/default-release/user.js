////////////////////////	実験的な about:config	////////////////////////
// user_pref("",true);     // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->

// user_pref("media.videocontrols.picture-in-picture.enable-when-switching-tabs.enabled",true);      // pip
// user_pref("browser.urlbar.keepPanelOpenDuringImeComposition",true);       // IME 変換中に結果を表示
user_pref("network.cookie.sameSite.laxByDefault",true);                   //
user_pref("network.cookie.sameSite.noneRequiresSecure",true);             //
user_pref("network.cookie.sameSite.schemeful",true);                      //

////////////////////////	about:config	////////////////////////

user_pref("accessibility.browsewithcaret_shortcut.enabled",false);        // キャレットブラウズモード (F7キー) の有効化
user_pref("alerts.showFavicons",true);                                    // Push通知 ファビコン

user_pref("beacon.enabled",false);                         // 位置情報
user_pref("geo.enabled",false);                            // 位置情報

user_pref("browser.aboutConfig.showWarning",false);        // about:configの警告を表示
user_pref("browser.bookmarks.autoExportHTML",true);        // ブックマーク
user_pref("browser.link.open_newwindow.restriction",2);    // JavaScript で開くウィンドウの扱い (0:「browser.link.open_newwindow」に従う 1:新規ウィンドウ 2:窓の大きさやツールバーの設定のあるものは新しい窓で開き、それ以外は「browser.link.open_newwindow」に従う。

user_pref("browser.cache.disk.enable",false);              // cache
user_pref("browser.cache.disk_cache_ssl",false);           // cache

user_pref("browser.download.alwaysOpenPanel",false);                      // right-click on the downloads button  ->  ダウンロード開始時にパネルを表示する
user_pref("browser.download.always_ask_before_handling_new_types",true);  // オプション  ->  一般  ->  ファイルとプログラム  ->  プログラム  ->  ファイルを開くか保存するか確認する
user_pref("browser.download.improvements_to_download_panel",false);       //
user_pref("browser.download.panel.shown",true);                           //
user_pref("browser.download.autohideButton",false);                       // right-click on the downloads button  ->  履歴がないときはボタンを非表示にする

// user_pref("browser.newtabpage.activity-stream.feeds.section.highlights",false);          // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->  ハイライト（保存したり訪れたりしたサイト）
// user_pref("browser.newtabpage.activity-stream.feeds.snippets",false);                    // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->  スニペット（Mozilla と Firefox に関する最新情報）
// user_pref("browser.newtabpage.activity-stream.feeds.topsites",true);                     // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->  トップサイト（よく訪れるサイト）
user_pref("browser.newtabpage.activity-stream.showSearch",true);                         // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->  ウェブ検索
user_pref("browser.newtabpage.activity-stream.showSponsored",false);                     // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->
user_pref("browser.newtabpage.activity-stream.showSponsoredTopSites",false);             // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->
user_pref("browser.newtabpage.activity-stream.topSitesRows",4);                          // オプション  ->  ホーム  ->  Firefox Home コンテンツ  ->  行数
user_pref("browser.newtabpage.activity-stream.improvesearch.handoffToAwesomebar",false); // about:newtab の検索時のロケーションバー


user_pref("browser.pocket.enabled",false);                 // pocket の有効化
user_pref("browser.search.openintab",true);                // 検索バー を新しいタブで開く
user_pref("browser.sessionstore.max_tabs_undo",50);        // 閉じたタブ を記憶できる数
user_pref("browser.send_pings.require_same_host",true);    // ホストが一致する場合にのみpingを送信（同じWebサイト）

user_pref("browser.tabs.allowTabDetach",false);            // タブを切り離し、新しいウィンドウで開く
user_pref("browser.tabs.closeWindowWithLastTab",false);    // 最後のタブを閉じたときブラウザも終了する
user_pref("browser.tabs.loadBookmarksInTabs",true);        // ブックマークを新しいタブで開く
user_pref("browser.tabs.loadInBackground",false);          // オプション  ->  一般  ->  タブ  ->  リンクを新しいタブで開く時、すぐにそのタブに切り替える
user_pref("browser.tabs.warnOnClose",true);                // オプション  ->  一般  ->  タブ  ->  同時に複数のタブを閉じる場合は確認する
user_pref("browser.tabs.maxOpenBeforeWarn",2);             // タブを同時に開こうとした際に警告をだす数

user_pref("browser.urlbar.suggest.topsites",false);        // オプション  ->  プライバシーとセキュリティ  ->  ブラウザープライバシー  ->  アドレスバー  ->  トップサイト
user_pref("browser.urlbar.suggest.history",false);         // オプション  ->  プライバシーとセキュリティ  ->  ブラウザープライバシー  ->  アドレスバー  ->  ブラウジング履歴

user_pref("browser.zoom.siteSpecific",false);              // サイトごとの拡大・縮小を記憶する

user_pref("devtools.chrome.enabled",true);                 // 開発ツール (CSS etc..)
user_pref("devtools.debugger.remote-enabled",true);        // 開発ツール (CSS etc..)
user_pref("dom.disable_window_move_resize",true);          // (JavaScriptによる)ウィンドウの移動･リサイズ の無効化
user_pref("dom.security.https_only_mode",false);           // オプション  ->  プライバシーとセキュリティ  ->  HTTPS-Only モード  ->  すべてのウィンドウで HTTPS-Only モードを有効にする

user_pref("extensions.update.interval",10800);             // アドオンの更新間隔 (1h = 3600)
user_pref("extensions.webextensions.restrictedDomains","accounts-static.cdn.mozilla.net,accounts.firefox.com,addons.cdn.mozilla.net,api.accounts.firefox.com,content.cdn.mozilla.net,discovery.addons.mozilla.org,install.mozilla.org,oauth.accounts.firefox.com,profile.accounts.firefox.com,sync.services.mozilla.com");			//

user_pref("font.name.monospace.ja",           "Roboto Mono,  Liberation Mono,  IPAゴシック,   Takaoゴシック");     // 等幅
user_pref("font.name.monospace.x-western",    "Roboto Mono,  Liberation Mono,  IPAゴシック,   Takaoゴシック");     // 等幅
user_pref("font.name.sans-serif.ja",          "Roboto Flex,  Liberation Sans,  IPA Pゴシック, Takao Pゴシック");   // ゴシック   (ひげ飾り 無し)
user_pref("font.name.sans-serif.x-western",   "Roboto Flex,  Liberation Sans,  IPA Pゴシック, Takao Pゴシック");   // サンセリフ (ひげ飾り 無し)
user_pref("font.name.serif.ja",               "Roboto serif, Liberation Serif, IPA P明朝,    Takao P明朝");      // 明朝体 (ひげ飾り 有り)
user_pref("font.name.serif.x-western",        "Roboto serif, Liberation Serif, IPA P明朝,    Takao P明朝");      // セリフ (ひげ飾り 有り)

user_pref("full-screen-api.warning.timeout",0);                 // HTML5動画のフルスクリーン警告非表示

user_pref("general.smoothScroll.msdPhysics.enabled", true);     //

user_pref("intl.accept_languages","ja");                        // オプション  ->  一般  ->  言語と外観  ->  言語     // Webページの言語設定

user_pref("layout.css.system-ui.enabled",false);                // system-ui
user_pref("layout.css.visited_links_enabled",false);            // オプション  ->  一般  ->  言語と外観  ->  フォントと配色  ->  配色設定  ->  システムの配色を使用する   / 訪問済みのリンクの色を変える
// user_pref("layout.css.always_underline_links",true);           // オプション  ->  一般  ->  ブラウジング  ->  常にリンクに下線をつける
user_pref("widget.gtk.overlay-scrollbars.enabled",false);       //　オプション  ->  一般  ->  ブラウジング  ->  常にスクロールバーを表示する

// user_pref("mousewheel.acceleration.factor", 15);        //
// user_pref("mousewheel.min_line_scroll_amount", 15);     //

user_pref("mousewheel.with_alt.action",0);                 // ━┓
user_pref("mousewheel.with_control.action",0);             // ━┫
user_pref("mousewheel.with_meta.action",0);                // ━╋━ ( 0:"何もしない" / 1:"スクロール" / 2:"進む or 戻る" / 3:"拡大 or 縮小" )
user_pref("mousewheel.with_shift.action",0);               // ━┫
user_pref("mousewheel.with_win.action",0);                 // ━┛

// user_pref("network.dns.disablePrefetch",false);             // DNS Prefetch の無効化
// user_pref("network.dns.disablePrefetchFromHTTPS",false);    // DNS Prefetch の無効化
user_pref("network.dns.echconfig.enabled",true);           // ECH (Encrypted Client Hello)
user_pref("network.dns.http3_echconfig.enabled",true);     // ECH (Encrypted Client Hello)
user_pref("network.dns.use_https_rr_as_altsvc",true);      // ECH (Encrypted Client Hello)

user_pref("network.http.referer.trimmingPolicy",2);        // 同一のオリジンへ送るリファラのトリミングの制御   (0: 完全なURIを送信   / 1: スキーム、ホスト、ポート、パス   / 2: 1からパスを除いたもの)
user_pref("network.http.referer.XOriginTrimmingPolicy",2); // 異なるオリジンへ送るリファラのトリミングの制御   (0: 完全なURIを送信   / 1: クエリ文字列を除いたURLを送信   / 2: オリジンのみを送信する)

user_pref("network.IDN_show_punycode",true);               // ホモグラフ攻撃 (homograph attack) 対策
user_pref("network.prefetch-next",false);                  // Prefetch の有効化

user_pref("network.trr.mode",3);                           // "Trusted Recursive Resolver" の挙動 ( 0: defaultでTRRを使わない / 1: より速い方を使用 / 2: TRRを優先的に使い普通のDNSも使う / 3: TRRだけを使う )
user_pref("network.trr.wait-for-portal",true);             //


// "https://blog.halpas.com/archives/2938" / "https://en.wikipedia.org/wiki/Public_recursive_name_server"

// user_pref("network.trr.bootstrapAddress","1.1.1.2");                                // Cloudflare
// user_pref("network.trr.uri","https://security.cloudflare-dns.com/dns-query");       // Cloudflare
user_pref("network.trr.bootstrapAddress","208.67.222.222");                         // OpenDNS (Cisco)
user_pref("network.trr.uri","https://doh.opendns.com/dns-query");                   // OpenDNS (Cisco)

// user_pref("privacy.webrtc.hideGlobalIndicator",true);                     // ???
user_pref("permissions.default.camera",2);                                //0 オプション  ->  プライバシーとセキュリティ  ->  許可設定  ->  カメラ    ( 0:Ask / 1.Always / 2.Never )
user_pref("permissions.default.desktop-notification",2);                  //0 オプション  ->  プライバシーとセキュリティ  ->  許可設定  ->  通知      ( 0:Ask / 1.Always / 2.Never )
user_pref("permissions.default.geo",2);                                   //0 オプション  ->  プライバシーとセキュリティ  ->  許可設定  ->  位置      ( 0:Ask / 1.Always / 2.Never )

user_pref("privacy.query_stripping.enabled",true);                        // パラメータ除去
user_pref("privacy.resistFingerprinting.block_mozAddonManager",true);     // アドオン無効化解除

user_pref("browser.formfill.enable",false);                               //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  検索やフォームの入力履歴を記憶させる
user_pref("places.history.enabled",false);                                //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  表示したページとダウンロード履歴 を有効にする

user_pref("privacy.sanitize.sanitizeOnShutdown",true);                    //f オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する
user_pref("privacy.clearOnShutdown.cache",true);                          //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->   履歴   ->  キャッシュ
user_pref("privacy.clearOnShutdown.cookies",false);                       //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->   履歴   ->  cookie
user_pref("privacy.clearOnShutdown.sessions",false);                      //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->   履歴   ->  現在のログイン情報
user_pref("privacy.clearOnShutdown.downloads",true);                      //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->   履歴   ->  表示したページとダウンロードの履歴		/ (downloads / history は連動させる)
user_pref("privacy.clearOnShutdown.history",true);                        //t オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->   履歴   ->  表示したページとダウンロードの履歴		/ (downloads / history は連動させる)
user_pref("privacy.clearOnShutdown.offlineApps",false);                   //f オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->  データ  ->  Web サイトのオフライン作業用データ (Cookie 内部のサイトデータ、Service Worker)		/※ 消すとログイン状態が全部外れて大変
user_pref("privacy.clearOnShutdown.siteSettings",false);                  //f オプション  ->  プライバシーとセキュリティ  ->    履歴    ->  Firefox終了時に履歴を消去する  ->  データ  ->  サイトの設定	// ロケーションバーアイコン  ->  ページの情報  ->  サイト別設定		/※ 消すとログイン状態が全部外れて大変

user_pref("security.mixed_content.block_active_content",true);            // スクリプト、スタイルシート、プラグインコンテンツ、インラインフレーム、Webフォント、WebSockets
user_pref("security.mixed_content.block_display_content",true);           // 画像、音声、動画などの静的コンテンツ
user_pref("security.mixed_content.block_object_subrequest",true);         //

user_pref("services.sync.prefs.sync.services.sync.engine.addons",true);        // オプション  ->  Sync  ->  同期  ->  アドオン
user_pref("services.sync.prefs.sync.services.sync.engine.bookmarks",true);     // オプション  ->  Sync  ->  同期  ->  ブックマーク
user_pref("services.sync.prefs.sync.services.sync.engine.history",false);      // オプション  ->  Sync  ->  同期  ->  履歴
user_pref("services.sync.prefs.sync.services.sync.engine.passwords",true);     // オプション  ->  Sync  ->  同期  ->  ログイン情報とパスワード
user_pref("services.sync.prefs.sync.services.sync.engine.prefs",true);         // オプション  ->  Sync  ->  同期  ->  オプション
user_pref("services.sync.prefs.sync.services.sync.engine.tabs",false);         // オプション  ->  Sync  ->  同期  ->  開いたタブ


user_pref("toolkit.legacyUserProfileCustomizations.stylesheets",true);    // userChrome.css を有効
user_pref("toolkit.tabbox.switchByScrolling",true);                       // タブ上でのホイールによる移動の有効化

user_pref("ui.submenuDelay",25);                                          // 【新規作成】サブメニュー表示 の遅延時間(マイクロ秒)


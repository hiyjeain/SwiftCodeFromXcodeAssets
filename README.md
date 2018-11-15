# SwiftCodeFromXcodeAssets

## Introduce
This is just a tool for creating Swift extension code from Xcode's **Assets.xcassets** resources.

## Example
Consider a project structure like

```
|____YourProject
| |____Assets.xcassets
| | | |____home_default.imageset
| | | | |____home_default@2x.png
| | | | |____home_default@3x.png
| | | | |____Contents.json
| | | | |____home_default.png
| | | |____like_default.imageset
| | | | |____like_default.png
| | | | |____Contents.json
| | | | |____like_default@2x.png
| | | | |____like_default@3x.png
| | | |____home_selected.imageset
| | | | |____Contents.json
| | | | |____home_selected.png
| | | | |____home_selected@2x.png
| | | | |____home_selected@3x.png
| | | |____like_selected.imageset
| | | | |____like_selected@3x.png
| | | | |____like_selected@2x.png
| | | | |____Contents.json
| | | | |____like_selected.png
| | |____AppIcon.appiconset
| | | |____icon.png
| | | |____Spotlight@3x.png
| | | |____Spotlight@2x.png
| | | |____icon@2x.png
| | | |____Contents.json
| | | |____icon@3x.png
| | | |____AppIcon@3x.png
| | | |____AppIcon@2x.png
| | |____Colors
| | | |____C1.colorset
| | | | |____Contents.json
| | | |____C6.colorset
| | | | |____Contents.json
| | | |____C7.colorset
| | | | |____Contents.json
| | | |____Transparent.colorset
| | | | |____Contents.json
| | | |____C2.colorset
| | | | |____Contents.json
| | | |____C3.colorset
| | | | |____Contents.json
| | | |____Contents.json
| | | |____C8.colorset
| | | | |____Contents.json
| | | |____C5.colorset
| | | | |____Contents.json
| | | |____C4.colorset
| | | | |____Contents.json
| | |____Contents.json
|... Other project files
```

This tool will generate code:

```
import Foundation
import UIKit

extension UIColor {
    
    public static let HOME_DEFAULT = UIImage(named: "home_default")
    public static let HOME_SELECTED = UIImage(named: "home_selected")
    public static let LIKE_DEFAULT = UIImage(named: "like_default")
    public static let LIKE_SELECTED = UIImage(named: "like_selected")    
}

```

and

```
import Foundation
import UIKit

extension UIColor {
    public static let C1 = UIColor(named: "C1")
    public static let C2 = UIColor(named: "C2")
    public static let C3 = UIColor(named: "C3")
    public static let C4 = UIColor(named: "C4")
    public static let C5 = UIColor(named: "C5")
    public static let C6 = UIColor(named: "C6")
    public static let C7 = UIColor(named: "C7")
    public static let C8 = UIColor(named: "C8")
    public static let TRANSPARENT = UIColor(named: "Transparent")
    
}
```

Thus we can use resources like 

```
self.navigationBar.tintColor = UIColor.C1
self.navigationBar.shadowImage = UIImage.HOME
```

## Usage

```
python3 app.py '~/YourProject'
```



import SwiftUI

/// Starter project tokens. These values are project conventions,
/// not universal Apple HIG constants.
enum AppSpacing {
    static let xxs: CGFloat = 4
    static let xs: CGFloat = 8
    static let sm: CGFloat = 12
    static let md: CGFloat = 16
    static let lg: CGFloat = 24
    static let xl: CGFloat = 32
    static let xxl: CGFloat = 48
}

enum AppRadius {
    static let contentCard: CGFloat = 16
}

enum AppMotion {
    static let state = Animation.smooth
    static let interaction = Animation.snappy
}

enum AppColor {
    static let brandAccent = Color.accentColor
}

export declare function getRandomInt(min: number, max: number): number;
export declare function getRandomItem<T>(array: ReadonlyArray<T>): T;
export declare const stdScalarFakers: {
    Int: () => number;
    Float: () => number;
    String: () => string;
    Boolean: () => boolean;
    ID: () => string;
};
export declare function fakeValue(type: any, options?: any, locale?: any): any;
